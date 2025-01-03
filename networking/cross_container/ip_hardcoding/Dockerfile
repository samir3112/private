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

# copy everything to /app directory
COPY . .

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker stop network-app
# docker stop mongodb
# docker rm mongodb
# prior that lets run mongo container
# docker run -d --name mongodb mongo
# see mongo container running
# docker ps -a
# docker inspect mongodb
# look for "NetworkSettings" -> "IPAddress"
# change mongo_pass.py for IP
# docker build -t cbagade/py-networking:v2 .
# docker run -p 5000:5000 -d --name network-app --rm cbagade/py-networking:v2
# docker logs network-app -f
# ensure content type from postman is JSON
# GET - http://localhost:5000/api/v1/fruits - fetch nothing
# POST - http://localhost:5000/api/v1/fruits
# {
#    "fruitName":"Banana",
#    "price": 89,
#    "oraganic": true
# }
# GET - http://localhost:5000/api/v1/fruits
# docker stop network-app
# docker stop mongodb
# docker rm mongodb
