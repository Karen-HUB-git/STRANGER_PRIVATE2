@echo off
pip install pystyle requests
echo Modules installed successfully! Do you want to run Vortex? y/n
set /p userChoice=Enter your choice (y/n): 
if "%userChoice%"=="y" (
    python main.py
) else (
    echo Bye.
)
pause
