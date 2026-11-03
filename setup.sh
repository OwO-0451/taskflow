#!/usr/bin/env bash
set -e
echo "=== Настройка окружения TaskFlow ==="
python -m venv venv
if [ -x "venv/Scripts/python.exe" ]; then
  PY="venv/Scripts/python.exe"
else
  PY="venv/bin/python"
fi
"$PY" -m pip install flask flask-sqlalchemy python-dotenv
echo "Окружение готово"