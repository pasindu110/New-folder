#!/usr/bin/env sh
set -e

# Initialize database if not present
if [ ! -f "books.db" ]; then
  echo "Initializing SQLite database..."
  python init_db.py
fi

echo "Starting Gunicorn on port ${PORT:-8080}..."
exec gunicorn -w ${GUNICORN_WORKERS:-2} -b 0.0.0.0:${PORT:-8080} app:app


