# Dockerfile is needed to create image
# Consistof instructions like FROM, EXPOSE, WORKDIR etc
# There are arguments supplied to these instructions like - 
# FROM (which is instruction) python:3.12-slim (which is argument)
# 

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

# copy app.py to /app directory
COPY app.py .

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-first-prog:v1 .

# docker run cbagade/py-first-prog:v1
# container is running but if you do 
# curl http://127.0.0.1:5000/
# you get nothing
# The IP of container is not known to outside world.
# docker containers run in its own environment, which is sitting on your localhost
# so the application won't be accessble on your localhost
# docker inspect <container_id>
# Open another terminal and run curl http://<IP_addr>:5000 and you can see page


# We can map port of container to my localhost to see the site with
# -p option - 

# map port of host to that of container (host port is mapped to container, container port is mapped to application)
# docker run -p 5000:5000 cbagade/py-first-prog:v1
# curl http://localhost:5000/ (access application on host port which is mapped to container)
# stop and remove the previous container
# docker stop 767b5dd18fb5
# docker rm 767b5dd18fb5
# also -d is run container in detach modes
# docker run -d -p 5000:5000 cbagade/py-first-prog:v1 (in detached mode)
# curl http://localhost:5000/ (access application on host port which is mapped to container)

# running same application on diff port (port should be unique)
# docker run -p 5001:5000 cbagade/py-first-prog:v1
# http://localhost:5001/ (access application on host port which is mapped to container)

# docker ps -a
# enter the container
# docker exec -it <container_id> /bin/bash (or docker exec -it <container_id> /bin/bash)
# ls /app
# docker stop <container_id>
# docker rm <container_id>
# image can be seen on docker hub

# make changes to app.js
# docker build -t cbagade/py-first-prog:v2 .
# docker run -p 5000:5000 cbagade/py-first-prog:v2
# http://localhost:5000/ (access application on host port which is mapped to container)

# push docker image to docker hub
# docker push cbagade/py-first-prog:v1