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


# docker build -t cbagade/cm-demo:v1 .
# docker push cbagade/cm-demo:v1
