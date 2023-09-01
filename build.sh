#!/usr/bin/env bash
# exit on error
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install Django Pillow psycopg2-binary dj-database-url python-dotenv
python3.9 manage.py collectstatic --noinput
python manage.py migrate