#!/bin/bash

sudo service nginx stop
sudo sed -i 's/user\s*nginx;/user nginx nginx;/' /etc/nginx/nginx.conf
sudo sed -i 's/listen\s*80;/listen 8080;/g' /etc/nginx/sites-available/default
sudo service nginx start

