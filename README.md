# Webservices-Docker-101

Addition of 2 numbers webservice using python

## Table of contents
* [Description](#description)
* [Technologies](#technologies)

## Description
This project is simple Addition of two numbers project in python. I build this project to learn Docker.
I deployed this project in docker container now anyone can access this webservice from anywhere.
	
## Technologies
Project is created with:
* Python version: 3.9.6
* Cherrypy version: 18.6.1
* Docker version: 20.10.8
	
## Deployment

To deploy this project run

```bash
  $ docker run -dp 5000:5000 tejasjogi/webapp:mywebapp
```
OR

```
  $ sudo docker run -dp 5000:5000 tejasjogi/webapp:mywebapp
```

## Authors

[TejasJogi](https://www.github.com/TejasJogi)
