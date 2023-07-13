# project4-phonebook_microservice
This project is a PhoneBook WebApplication microservices. 
You can **add** and **search** PhoneNubmer in this application.


# Technologies and Tools
This app has 5 Technologies and Tools:
1) Python(Flask)
2) Jenkins(Scripted-syntax pipeline)
3) Kubernetes(Deployment, Service, Secret)
4) MySQL
5) Nginx(porxy)


# Versions and Branches
This projcet has 2 different branches :
1) main : Complete project with Secret and Security .
2) withoutSecret: project without any Secret .


# Startup and Run
you can Run this project with kubernetes yaml files :
```
kubectl apply -f services.yaml
```
```
kubectl apply -f deployments.yaml
```
```
kubectl apply -f db_pass_secret.yaml
```

**or, if you change and customize Jenkinsfile for your host , you can use it to Run project**
