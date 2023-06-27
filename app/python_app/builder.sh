#!/usr/bin/bash

##Create Docker Image (python dockerimage):

docker build -t babaknasrolahy/project4-python:latest -f ./app/python_app/python-dockerfile .

##Push Docker Image (python dockerimages)

echo $babakPassword | sudo -S docker push babaknasrolahy/project4-python:latest
