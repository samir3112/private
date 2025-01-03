# base image, this will provide a python environment for out application to run
# slim version of python image
FROM python:3.12-slim

# install curl 
RUN apt update -y && apt install curl -y


# on to OS of above base image, we saying /app should be our working directory
# its like cd /app
WORKDIR /app

# copy everything to /app directory inside container
COPY app.py .

# for print statements
ENV PYTHONUNBUFFERED=1

# docker build -t cbagade/task-app:v1 .
# docker push cbagade/task-app:v1