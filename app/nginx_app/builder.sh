#!/usr/bin/bash

##Create Docker Image (nginx dockerimage):

docker build -t babaknasrolahy/project4-nginx:latest -f nginx-dockerfile . 

##Push Docker Image (nginx dockerimages)

docker push babaknasrolahy/project4-nginx:latest
