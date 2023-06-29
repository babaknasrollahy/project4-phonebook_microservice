#!/usr/bin/bash

##Create Docker Image (worker dockerimage):

docker build -t babaknasrolahy/project4-worker:latest -f ./app/worker_app/worker-dockerfile . 

##Push Docker Image (worker dockerimages)

sudo -S docker push babaknasrolahy/project4-worker:latest
