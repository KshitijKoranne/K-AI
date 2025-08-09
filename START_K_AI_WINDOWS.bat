@echo off
cls
echo.
echo =================================================
echo    🚀 K-AI Pharmaceutical Chatbot Launcher
echo =================================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running. Please start Docker Desktop and try again.
    echo.
    pause
    exit /b 1
)

echo ✅ Docker is running
echo.

REM Navigate to deployment directory
cd /d "%~dp0deployment"

echo 🔧 Starting K-AI services...
docker-compose -f docker-compose.yaml up -d

echo.
echo ⏳ Waiting for services to start...
timeout /t 15 /nobreak >nul

echo.
echo 🌐 Opening K-AI in your browser...
start "" "http://localhost:5173"

echo.
echo =================================================
echo    🎉 K-AI Pharmaceutical Chatbot is running!
echo =================================================
echo.
echo 📱 Access your chatbot at: http://localhost:5173
echo.
echo 📋 To stop K-AI later, run:
echo    docker-compose -f deployment/docker-compose.yaml down
echo.
echo 💡 Your OpenRouter API key is already configured
echo 📚 Ready to chat about pharmaceutical SOPs and GMP!
echo.
echo =================================================

pause