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

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-data-vol:v1 .
# docker run -d  -p 5000:5000 --name manage-data --rm cbagade/py-data-vol:v1 (--rm flag will remove container when its not running)
# docker logs manage-data -f
# GET http://localhost:5000/api/v1/fruits 
# POST  http://localhost:5000/api/v1/fruits -d {"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}
# GET http://localhost:5000/api/v1/fruits 
# docker stop manage-data
# docker run -p 5000:5000 -d --name manage-data --rm cbagade/py-data-vol:v1
# GET http://localhost:5000/api/v1/fruits  -> changes are gone
# data was available till container was running