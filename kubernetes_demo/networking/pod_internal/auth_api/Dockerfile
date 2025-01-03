# base image, this will provide a python environment for out application to run
# slim version of python image
FROM python:3.12-slim

# install curl 
RUN apt update -y && apt install curl -y

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

# for print statements
ENV PYTHONUNBUFFERED=1


ENTRYPOINT python app.py


# docker build -t cbagade/pykub-demo-auth:latest .
# docker push cbagade/pykub-demo-auth:latest