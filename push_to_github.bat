@echo off
echo 🚀 Pushing CyberBook Hub to GitHub...
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed. Please install Git first:
    echo    https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Initialize git repository
echo 📁 Initializing git repository...
git init -b main

REM Add all files
echo 📝 Adding files to git...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "Initial commit: CyberBook Hub vulnerable web app with auto-deployment"

echo.
echo ✅ Ready to push to GitHub!
echo.
echo 📋 Next steps:
echo 1. Create a new repository on GitHub.com
echo 2. Copy the repository URL
echo 3. Run these commands:
echo.
echo    git remote add origin YOUR_GITHUB_URL_HERE
echo    git push -u origin main
echo.
echo 🌐 Then deploy on Render:
echo 1. Go to render.com
echo 2. Connect your GitHub repository
echo 3. Render will auto-deploy using render.yaml
echo.

pause
