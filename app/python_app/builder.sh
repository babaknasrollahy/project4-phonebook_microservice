#!/usr/bin/bash
echo "--------------------------------------------------------"
echo `pwd`
echo "--------------------------------------------------------"
##Create Docker Image (python dockerimage):

docker build -t babaknasrolahy/project4-python:latest -f python-dockerfile . 

##Push Docker Image (python dockerimages)

docker push babaknasrolahy/project4-python:latest
