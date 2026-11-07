@echo off
title ScamShield NLP API Server
echo ===================================================
echo   Starting ScamShield FastAPI Server...
echo ===================================================
cd /d "%~dp0"
python -m uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
pause
