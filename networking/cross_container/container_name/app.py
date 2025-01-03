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
from mongo_pass import mongo_connection_string
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(mongo_connection_string)
# Database 
db = client.get_database('fruits_db') 
# Table  (collection)
fruits_coll = db.fruits_coll


@app.post("/api/v1/fruits")
def create_fruits():
    request_data = request.get_json()
    fruits_coll.insert_one(request_data) 
    return {"message":"ok"}, 201

@app.get("/api/v1/fruits")
def get_all_fruits(): 
    query_results = fruits_coll.find({}, {'_id': False})
    return list(query_results), 200