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

# for named volume we don't need this
# this will be done with command
# VOLUME [ "/app/userchanges" ]

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker volume prune
# docker build -t cbagade/py-data-vol:v3 .
# docker push cbagade/py-data-vol:v3
# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# docker ps -a
# observe a volume created
# docker volume ls
# docker exec -it named-vol /bin/bash
# cd userchanges
# make some changes to file on your computer (touch chandra.txt)
# docker stop named-vol
# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# docker exec -it named-vol /bin/bash
# check the changes and this time changes are retained
# named volumes survives container restarts
# POST http://localhost:5000/api/v1/fruits  -d {"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}
# this action will create a file inside container
# Also hit on GET http://localhost:5000/api/v1/fruits
# docker stop named-vol
# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# Hit on GET http://localhost:5000/api/v1/fruits
# changes are retained