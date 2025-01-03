# venv is a folder where all packages gets installed
# https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
# rm -rf venv
# sudo apt install python3.12-venv
# python3.12 -m venv .venv
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

from flask import Flask, request
import flask
import json
import os


app = Flask(__name__)

folder_name = os.environ.get('USERCHANGES_FOLDER')
path_name = f"./{folder_name}/fruits.json"

# read JSON file
# Opening JSON file
with open("./data/fruits_data.json") as json_file:
    fruits_json = json.load(json_file)


@app.get("/api/v1/fruits/error")
def get_error():
    os._exit(1)


@app.get("/api/v1/fruits")
def get_all_fruits():
    print("get_all_fruits() :: entered")
    if os.path.exists(path_name):
        return flask.send_file(path_name), 200
    return {"message":"fruits not found"}, 404


@app.post("/api/v1/fruits")
def create_a_fruit():
    print(f"create_a_fruit():: path_name is {path_name}")
    fruit_from_request = request.get_json()
    id_for_new_fruit = len(fruits_json)
    fruit_from_request["id"] = id_for_new_fruit
    fruits_json.append(fruit_from_request)
    if os.path.exists(path_name):
        os.remove(path_name)
    os.makedirs(os.path.dirname(path_name), exist_ok=True)
    with open(path_name, "w") as f:
        json.dump(fruits_json, f)
    return fruit_from_request, 201