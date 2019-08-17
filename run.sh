#!/bin/bash
git pull origin master
. bin/activate
git pull origin master
pip install -r requirements.txt
./manage.py runserver 0.0.0.0:8000

