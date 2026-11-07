@echo off
title ScamShield Clipboard Phishing Shield
echo ===================================================
echo   Starting ScamShield Clipboard ^& Browser Shield
echo ===================================================
cd /d "%~dp0"
python src\clipboard_guard.py
pause
