from flask import Flask, request
from mongo_pass import mongo_connection_string
from pymongo import MongoClient

app = Flask(__name__)
print(f"mongo connection string is {mongo_connection_string}")
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