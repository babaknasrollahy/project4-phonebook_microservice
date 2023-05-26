#!/usr/bin/bash

##Create Docker Image (worker dockerimage):

docker build -t babaknasrolahy/project4-worker:latest -f worker-dockerfile . 

##Push Docker Image (worker dockerimages)

docker push babaknasrolahy/project4-worker:latest
