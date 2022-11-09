#!/bin/bash

python3.8 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r /apps/hackyeah_ml/requirements.txt
python /apps/hackyeah_ml/manage.py runserver 0.0.0.0:8080