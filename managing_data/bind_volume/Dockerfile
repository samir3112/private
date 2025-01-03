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


# docker stop named-vol
# docker volume prune
# docker volume rm namedvol
# docker build -t cbagade/py-data-vol:v4 .
# docker run -p 5000:5000 -d --name bind-vol -v "/home/chandra/docker-kubernetes-learnings/managing_data/bind_volume/userchanges:/app/userchanges" --rm cbagade/py-data-vol:v4
# OR TRY THIS (newwer way)
# docker run -p 5000:5000 -d --name bind-vol --mount type=bind,source=/home/chandra/docker-kubernetes-learnings/managing_data/bind_volume/userchanges,target=/app/userchanges --rm cbagade/py-data-vol:v4

# GET http://localhost:5000/api/v1/demo_bind_vol
# now this volume with be mounted on /home/chandra/docker-kubernetes-learnings/managing_data/named_volume/userchanges
# any changes made to file inside container will be available at this path
# not for production