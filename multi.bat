@echo off
cd apirest
start python routes.py
cd ..
cls
start chrome http://127.0.0.1:8000/niveles/l