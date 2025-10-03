# CyberBook Hub 🔐

A modern vulnerable web application demonstrating various security vulnerabilities for educational purposes.

## ⚠️ Security Notice

**This application is intentionally vulnerable and should ONLY be used in isolated lab environments. Do not deploy to production or expose to the internet without proper security measures.**

## 🚀 Live Demo

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME)

## 🛠️ Features

- **Modern UI**: Purple-themed responsive design
- **SQL Injection**: Vulnerable search functionality
- **XSS Vulnerabilities**: Stored and reflected XSS
- **Cryptographic Failures**: Weak MD5 password hashing
- **Path Traversal**: Unsafe file download endpoint
- **Interactive Learning**: Hands-on vulnerability demonstrations

## 🏗️ Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open http://127.0.0.1:5000 in your browser

## 🌐 Deployment Options

### Heroku (Recommended)

1. **Fork this repository**
2. **Create a Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Initialize database on Heroku**
   ```bash
   heroku run python init_db.py
   ```

### Railway

1. **Connect your GitHub repository**
2. **Deploy automatically**
3. **Run database initialization**

### Render

1. **Create a new Web Service**
2. **Connect your GitHub repository**
3. **Set build command**: `pip install -r requirements.txt`
4. **Set start command**: `gunicorn app:app`

## 🔍 Vulnerabilities Demonstrated

### 1. SQL Injection
- **Location**: Search functionality (`/search`)
- **Payload**: `' OR '1'='1`
- **Flag**: `THM{sql_flag_ABC123}`

### 2. Cross-Site Scripting (XSS)
- **Location**: Book reviews (`/book/<id>`)
- **Payload**: `<script>alert('XSS')</script>`
- **Flag**: `THM{xss_flag_DEF456}`

### 3. Cryptographic Failures
- **Location**: Admin panel (`/admin`)
- **Issue**: Weak MD5 password hashing
- **Credentials**: `admin/password123`, `test/test`, `demo/demo`
- **Flag**: `THM{crypto_flag_MNO345}`

### 4. Path Traversal
- **Location**: Download endpoint (`/download`)
- **Payload**: `?file=../secret.txt`
- **Flag**: `THM{path_flag_JKL012}`

## 📁 Project Structure

```
cyberbook-hub/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization
├── generate_images.py  # Image generation script
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
├── static/
│   ├── style.css      # Modern CSS styling
│   ├── ui.js          # JavaScript functionality
│   └── images/        # Static images
├── templates/
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── search.html    # Search results
│   ├── book.html      # Book details
│   └── admin.html     # Admin panel
└── uploads/           # File upload directory
```

## 🎨 Customization

### Changing Colors
Edit `static/style.css` and modify the CSS variables:
```css
:root {
  --accent: #8b5cf6;        /* Primary color */
  --accent-light: #a78bfa;  /* Light accent */
  --bg: #1a1d29;            /* Background */
  --card: #252837;          /* Card background */
}
```

### Adding Vulnerabilities
1. Create new routes in `app.py`
2. Add corresponding templates
3. Update navigation in `base.html`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is for educational purposes only. Use responsibly and only in isolated environments.

## ⚡ Quick Start Commands

```bash
# Local development
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
python app.py

# Heroku deployment
heroku create your-app-name
git push heroku main
heroku run python init_db.py
```

## 🔗 Links

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)

---

**Remember**: This is a learning tool. Always practice responsible disclosure and use only in controlled environments! 🛡️
