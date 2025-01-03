# To install python on VSC and to set 3.12 as default follow
# https://www.linuxtuto.com/how-to-install-python-3-12-on-ubuntu-22-04/

# venv is a folder where all packages gets installed
# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
# rm -rf venv
# sudo apt install python3.11-venv
# python3.11 -m venv .venv      
# export PIP_BREAK_SYSTEM_PACKAGES=1
# python3 -m pip install --upgrade pip
# if you want to use .venv on ubuntu cli
# source .venv/bin/activate
# if you want to come out of .vnev on ubuntu cli
# deactivate
# if you want to use .venv on Visual Studio Code (VSC)
# (Once you created .venv on ubuntu or VCS), the VSC will show you a button to Select Interpreter
# Oe Ctrl + Shift + P and Select Interpreter in that box
# And select entry with .venv/bin/python
# When you do View - Terminal , it should show , something like
# Now all packages you install, with pip will reside in .venv
# (.venv) chandra@DESKTOP-NGKLJIG:~/py-docker-kubernetes-learnings/docker_demo$ 
# pip install -r requirements.txt

import os
from flask import Flask

app = Flask(__name__)

who_to_greet = os.environ.get("who_to_greet_env_var")

@app.get("/")
def get_greetings():
    greet_message = f"Hi {who_to_greet} , This is coming from container, Welcome to container world, again"
    return greet_message, 200

# to test this file, without docker
# pip install -r requirements.txt
# run following command
# flask run
# access on http://localhost:5000

# find env vars on running container
# docker inspect <container_id>