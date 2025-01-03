FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy everything to /app directory inside container
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-first-prog:v3 .
# pushing image to docker registry
# docker login -u <docker_hub_user>
# docker push cbagade/py-first-prog:v3
# map port of host to that of container (host port is mapped to container, container port is mapped to application)
# providing name to container
# docker run -d -p 5000:5000 --name py-demo cbagade/py-first-prog:v3
# looking at logs of container
# docker ps -a
# docker logs <container_id> -f
# on other terminal
# curl http://localhost:5000/fruits (access application on host port which is mapped to container)
# curl http://localhost:5000/fruits/orange (access application on host port which is mapped to container)
# docker stop py-demo
# docker rm py-demo