@echo off
call .venv\Scripts\activate.bat
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
pause
