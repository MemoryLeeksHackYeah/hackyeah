#!/bin/bash

# Prerequisites
gcloud secrets versions access latest --secret=google_maps_api  --format='get(payload.data)' | tr '_-' '/+' | base64 -d > /apps/hackyeah_ml/config/google_maps_api_key

# Running application
python3.8 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r /apps/hackyeah_ml/requirements.txt

export GOOGLE_CLOUD_PROJECT="memory-leeks-hackyeah"
export GOOGLE_APPLICATION_CREDENTIALS=~/.config/gcloud/application_default_credentials.json

python /apps/hackyeah_ml/manage.py runserver 0.0.0.0:8080