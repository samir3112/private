from flask import Flask, request
import flask
import json
import os


app = Flask(__name__)

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
    if os.path.exists("./userchanges/fruits.json"):
        return flask.send_file("./userchanges/fruits.json"), 200
    return {"message":"fruits not found"}, 404


@app.post("/api/v1/fruits")
def create_a_fruit():
    fruit_from_request = request.get_json()
    print(f"fruit_from_request is {fruit_from_request}")
    id_for_new_fruit = len(fruits_json)
    fruit_from_request["id"] = id_for_new_fruit
    fruits_json.append(fruit_from_request)
    if os.path.exists("./userchanges/fruits.json"):
        os.remove("./userchanges/fruits.json")
    os.makedirs(os.path.dirname("./userchanges/fruits.json"), exist_ok=True)
    with open("./userchanges/fruits.json", "w") as f:
        json.dump(fruits_json, f)
    return fruit_from_request, 201