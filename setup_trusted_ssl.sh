#!/bin/bash
# Setup Certbot for Let's Encrypt SSL

# 1. Install Certbot
sudo apt-get update
sudo apt-get install -y certbot

# 2. Get the certificate
# We use "--standalone" which requires Nginx to be temporarily stopped
docker-compose stop nginx
sudo certbot certonly --standalone -d burnassistai.online --non-interactive --agree-tos -m "$1"
docker-compose start nginx

# 3. Success! Certificates will be in /etc/letsencrypt/live/burnassistai.online/
echo "✅ SSL Certificate generated successfully!"
