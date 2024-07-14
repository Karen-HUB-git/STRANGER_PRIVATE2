@echo off
cls
echo Installing dependencies in 3 seconds...
timeout /t 3 /nobreak > nul
python -m pip install -r requirements.txt
echo.
timeout /t 1 /nobreak > nul
echo.
echo Done..!
echo.
echo You can start Nexus with python by typing 'python Nexus.py' in the terminal.

set /p "input=Start Nexus now? (y/n) -> "
if /i "%input%"=="y" (
    echo Starting Nexus...
    timeout /t 1 /nobreak > nul
    python Nexus.py
) else (
    echo Exiting...
    timeout /t 1 /nobreak > nul
)
exit
