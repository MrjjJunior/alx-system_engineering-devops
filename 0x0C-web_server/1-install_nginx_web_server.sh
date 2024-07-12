#!/usr/bin/env bash
# Script installs Nginx

sudo apt-get -y update
sudo apt-get -y install nginxm

echo "Hello World!" > /var/www/html/index.html

service ngnix start
sudo ufw allow 'Nginx HTTP'
service nginx restart

sudo chown -R "$USER":"$USER" /var/www/html
sudo chown -R 755 /var/ww

