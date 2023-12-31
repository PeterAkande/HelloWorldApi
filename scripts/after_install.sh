#!/usr/bin/env bash

# kill any servers that may be running in the background
sudo pkill -f runserver
sudo pkill -f gunicorn # Kill Gunicorn Server

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /srv/HelloWorldApi
# Copy the .env file to this directory
sudo cp /srv/hello-world-api-env/.env /srv/HelloWorldApi/.env

python3 -m venv venv

# activate virtual environment
source venv/bin/activate

install requirements.txt
pip install -r /srv/HelloWorldApi/requirements.txt

pip install psycopg2-binary
pip install gunicorn

# Tell Supervisor to Kill all instance
sudo supervisorctl stop hello-world-api
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start hello-world-api

# Reload Nginx
sudo nginx -s reload
