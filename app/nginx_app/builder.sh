#!/usr/bin/bash

##Create Docker Image (nginx dockerimage):

docker build -t babaknasrolahy/project4-nginx:latest -f ./app/nginx_app/nginx-dockerfile .

##Push Docker Image (nginx dockerimages)

sudo -S docker push babaknasrolahy/project4-nginx:latest
