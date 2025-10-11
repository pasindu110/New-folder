from flask import Flask, render_template, request, send_from_directory, abort
import sqlite3
import os

app = Flask(__name__)
DB = "books.db"
UPLOAD_FOLDER = "uploads"


def get_db_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_conn()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template('index.html', books=books)


# Vulnerable search (SQL Injection) - intentionally unsafe string concat
@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    q = ''
    if request.method == 'POST':
        q = request.form.get('query', '')
        conn = get_db_conn()
        # <-- intentionally vulnerable (do not do in real apps)
        sql = "SELECT * FROM books WHERE title LIKE '%" + q + "%' OR author LIKE '%" + q + "%'"
        try:
            results = conn.execute(sql).fetchall()
        except Exception:
            results = []
        conn.close()
    return render_template('search.html', results=results, query=q)


# Book page with stored XSS (reviews stored and rendered unsafely)
@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book(book_id):
    conn = get_db_conn()
    book = conn.execute("SELECT * FROM books WHERE id=?", (book_id,)).fetchone()
    if not book:
        conn.close()
        return "Book not found", 404

    # Get temporary message from query string (for reflected XSS)
    temp_msg = request.args.get('msg', '')

    if request.method == 'POST':
        review = request.form.get('review', '')
        # stored without sanitization -> stored XSS vulnerability
        conn.execute("INSERT INTO reviews (book_id, review) VALUES (?, ?)", (book_id, review))
        conn.commit()

    reviews = conn.execute("SELECT review FROM reviews WHERE book_id=?", (book_id,)).fetchall()
    conn.close()
    return render_template('book.html', book=book, reviews=reviews)


# IDOR / missing auth demo: admin panel (no auth required)
@app.route('/admin')
def admin():
    conn = get_db_conn()
    books = conn.execute("SELECT * FROM books").fetchall()
    # retrieve admin flag from flags table
    row = conn.execute("SELECT value FROM flags WHERE name='idor_flag'").fetchone()
    admin_flag = row['value'] if row else "NO_FLAG"
    # get users for cryptographic failure demo
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    # This page intentionally leaks admin secret (IDOR/missing-auth demo)
    return render_template('admin.html', books=books, admin_flag=admin_flag, users=users)


# Path traversal vulnerable download endpoint (no sanitization)
@app.route('/download')
def download():
    filename = request.args.get('file', '')
    if not filename:
        return "Specify ?file=filename", 400
    # Intentionally vulnerable: no normalization or path checks
    try:
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return f"Error: {e}", 404


# Utility endpoint for XSS exploitation demo (retrieves a flag by name)
@app.route('/get_flag/<name>')
def get_flag(name):
    conn = get_db_conn()
    row = conn.execute("SELECT value FROM flags WHERE name=?", (name,)).fetchone()
    conn.close()
    if not row:
        abort(404)
    return row['value']


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


