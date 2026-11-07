@echo off
title ScamShield NLP Web App
echo ===================================================
echo   Starting ScamShield NLP Web Application...
echo ===================================================
cd /d "%~dp0"

set PYTHON_EXE=C:\Users\Manu\OneDrive\Desktop\scamshield\venv\Scripts\python.exe

if exist "%PYTHON_EXE%" (
    echo Using Virtualenv Python: %PYTHON_EXE%
    "%PYTHON_EXE%" -m streamlit run src/app.py
) else (
    echo Using System Python
    python -m streamlit run src/app.py
)

pause
