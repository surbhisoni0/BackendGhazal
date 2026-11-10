#!/bin/sh
cd "$(dirname "$0")/backend"
[ -d venv ] || python3 -m venv venv
venv/bin/pip install -q -r requirements.txt
venv/bin/python app.py
