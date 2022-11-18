#!/bin/bash

python3.8 -m venv venv
source venv/bin/activate
pip install -r source/hackyeah_ml/requirements.txt

export GOOGLE_CLOUD_PROJECT="memory-leeks-hackyeah"
export GOOGLE_APPLICATION_CREDENTIALS=~/.config/gcloud/application_default_credentials.json

python source/hackyeah_ml/manage.py runserver 8080