@echo off
echo Starting CyberBook Hub...
echo.

REM Activate virtual environment
call .venv\Scripts\activate

REM Initialize database if needed
if not exist books.db (
    echo Initializing database...
    python init_db.py
)

REM Start the Flask application
echo Starting Flask server...
echo Open http://127.0.0.1:5000 in your browser
echo Press Ctrl+C to stop the server
echo.
python app.py

pause
