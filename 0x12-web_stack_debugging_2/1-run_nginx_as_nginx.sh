#!/bin/bash
# Stop nginx if it's already running
sudo service nginx stop

# Set nginx to run as nginx user
sudo sed -i 's/user\s*nginx;/user nginx nginx;/' /etc/nginx/nginx.conf

# Set nginx to listen on all active IPs on port 8080
sudo sed -i 's/listen\s*80;/listen 8080;/g' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx start
