@echo off
title ScamShield WhatsApp Guardian
echo ===================================================
echo   Starting ScamShield WhatsApp Notification Guardian
echo ===================================================
cd /d "%~dp0"
python src\whatsapp_guardian.py
pause
