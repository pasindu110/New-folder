#!/usr/bin/env python3
"""
PythonAnywhere deployment setup
This creates the flask_app.py file needed for PythonAnywhere
"""
import os

def create_flask_app():
    """Create flask_app.py for PythonAnywhere"""
    flask_app_content = '''#!/usr/bin/env python3
import sys
import os

# Add your project directory to Python path
project_dir = '/home/YOUR_USERNAME/mysite'  # Replace YOUR_USERNAME with your actual username
sys.path.append(project_dir)

# Change to project directory
os.chdir(project_dir)

# Import and run the Flask app
from app import app

if __name__ == "__main__":
    app.run()
'''
    
    with open('flask_app.py', 'w') as f:
        f.write(flask_app_content)
    
    print("✅ Created flask_app.py for PythonAnywhere")
    print("📝 Remember to:")
    print("   1. Replace YOUR_USERNAME with your actual PythonAnywhere username")
    print("   2. Upload flask_app.py to your PythonAnywhere files")
    print("   3. Set it as your WSGI file in Web tab")

if __name__ == "__main__":
    create_flask_app()

