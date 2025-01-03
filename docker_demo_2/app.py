from flask import Flask
import json

app = Flask(__name__)

with open('./data/fruits_data.json') as json_file:
    fruits_json = json.load(json_file)

@app.get("/fruits")
def get_all_fruits():
    print("get_all_fruits() :: entered")
    return fruits_json, 200

@app.get("/fruits/<string:fruit_name>")
def get_a_fruit(fruit_name):
    for fruit in fruits_json:
        print(f"get_a_fruit() :: fruit is {fruit}")
        if fruit["fruitName"].lower() == fruit_name.lower():
            return fruit, 200
    return {"message":f"Fruits with name {fruit_name} is not found"}, 401

