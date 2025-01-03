# base image, this will provide a python environment for out application to run
# slim version of python image
FROM python:3.12-slim

# expose 5000 port of container, to map the port of our application
EXPOSE 5000

# on to OS of above base image, we saying /app should be our working directory
# its like cd /app
WORKDIR /app

# copy requirements.txt file from local machine in /app directory
COPY requirements.txt .

# run pip install -r requirements.txt to install libraries
RUN pip install -r requirements.txt

# copy everything to /app directory inside container
COPY . .

# userchanges will be available inside container , since copied to container
# that directory will be mounted as volume
# but where that is available on host, is not something we can control
# we should be able to get that location with a command, though
# only local directory is copied to container along with files inside
# but mounting has nothing to do with local directory
VOLUME [ "/app/userchanges" ]

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-data-vol:v2 .
# docker push cbagade/py-data-vol:v2
# docker run -d -p 5000:5000  --name anonymous-vol --rm cbagade/py-data-vol:v2
# docker ps -a
# observe a volume created
# docker volume ls (docker volume prune and docker system prune)
# this volume will be mounted by docker system and that path can be find out by -
# docker inspect --type container -f '{{range $i, $v := .Mounts }}{{printf "%v\n" $v}}{{end}}' anonymous-vol
# sudo ls to path obtained by docker inspect command
# this will be path on host
# docker logs anonymous-vol -f
# 
# POST http://localhost:5000/api/v1/fruits -d {"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}
# this action will create a file inside container
# Also hit on GET http://localhost:5000/api/v1/fruits 
# go to the path obtained by docker inspect command (this will be on host)
# the file which was created on host and created inside container can be seen
# docker exec -it anonymous-vol /bin/bash
# cd userchanges
# touch new_file.json
# observe those changes on host system , on path , obtained via inspect command

# docker stop anonymous-vol
# docker run -p 5000:5000 -d --name anonymous-vol --rm cbagade/py-data-vol:v2
# following fetch nothings
# http://localhost:5000/api/v1/fruits 
# docker inspect --type container -f '{{range $i, $v := .Mounts }}{{printf "%v\n" $v}}{{end}}' anonymous-vol
# check the file and now changes are gone (also volume has gone)