@echo off
cd /d "%~dp0backend"
if not exist venv (python -m venv venv)
call venv\Scripts\pip install -q -r requirements.txt
echo Open http://localhost:3000
venv\Scripts\python app.py
pause
