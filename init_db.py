import sqlite3
import os

DB = "books.db"

# Remove existing DB if you want a fresh start (optional)
if os.path.exists(DB):
    os.remove(DB)

conn = sqlite3.connect(DB)
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    description TEXT
)
''')

c.execute('''
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    review TEXT
)
''')

c.execute('''
CREATE TABLE flags (
    name TEXT PRIMARY KEY,
    value TEXT
)
''')

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT
)
''')

# Insert sample books
books = [
    ("The Vulnerable Book", "Alice", "A book full of secrets and surprises."),
    ("SQL for Hackers", "Bob", "Try the search box—it's not safe."),
    ("Pathways of Code", "Charlie", "Contains hidden files behind the shelves.")
]
c.executemany("INSERT INTO books (title, author, description) VALUES (?, ?, ?)", books)

# Insert an example review (innocent)
c.execute("INSERT INTO reviews (book_id, review) VALUES (?, ?)", (2, "Crowd favorite — 5 stars."))

# Insert flags used by tasks
flags = [
    ("sql_flag",    "THM{sql_flag_ABC123}"),
    ("xss_flag",    "THM{xss_flag_DEF456}"),
    ("crypto_flag", "THM{crypto_flag_MNO345}"),
    ("path_flag",   "THM{path_flag_JKL012}")
]
c.executemany("INSERT INTO flags (name, value) VALUES (?, ?)", flags)

# Insert sample users with weak MD5 hashes (Cryptographic Failure demo)
import hashlib
users = [
    ("admin", hashlib.md5("password123".encode()).hexdigest()),
    ("user1", hashlib.md5("admin".encode()).hexdigest()),
    ("test", hashlib.md5("test".encode()).hexdigest()),
    ("demo", hashlib.md5("demo".encode()).hexdigest())
]
c.executemany("INSERT INTO users (username, password_hash) VALUES (?, ?)", users)

conn.commit()
conn.close()

# Create uploads folder and drop a secret file (used by path traversal)
os.makedirs('uploads', exist_ok=True)
with open(os.path.join('uploads', 'sample.txt'), 'w', encoding='utf-8') as f:
    f.write("Sample file for download.\n")
with open(os.path.join('uploads', 'secret.txt'), 'w', encoding='utf-8') as f:
    f.write("TOP_SECRET_FILE\nTHM{path_flag_JKL012}\n")

print("Database and upload files created (books.db + uploads/).")


