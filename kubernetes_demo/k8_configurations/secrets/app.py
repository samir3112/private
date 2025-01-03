from flask import Flask, request
# ensure string is in proper format
from mongopass import mongo_conn_string
from pymongo import MongoClient

# BSON stands for Binary JavaScript Object Notation.
# It's a binary-encoded format for JSON documents that was developed by MongoDB, used while
# storing data in mongo collection
from bson.json_util import dumps

# create flask app
app = Flask(__name__)
# create connection to mongo
print(f"{mongo_conn_string} is connection string")
client = MongoClient(mongo_conn_string)

# At top level on Atlas is cluster
# create a database
db = client.get_database('fruits_db')
# create collection
fruits_coll = db.fruits_coll


# create fruit
# get request data as json
# call insert_one method of collection, fruits_coll
# pass following data from request
# {"fruitName":"Alovera","from":"Tamilnadu","nutrients":"Vitamin B, Vitamin K","price":"200.50","organic":true,"description":"An avocado is a bright green fruit with a large pit and dark leathery skin. They're also known as alligator pears or butter fruit. Avocados are a favorite of the produce section. They're the go-to ingredient for guacamole dips."}
# since there will be bson object, at this point only "Ok" message (or call dumps() to convert to json)
# change name of fruit from postmane and submit 3 to 4 requests
# observe collection on atlas mongo

@app.post('/mongo/fruits')
def create_fruits_in_mongo():
    request_data = request.get_json()
    fruits_coll.insert_one(request_data) 
    return {"message":"ok"}, 201


# get from mongo
# call find method of collection, fruits_coll and pass 2 json, 1 is blank and second where _id is false to return doc without _id
# students should read doc to see diff versions of find method, like to return only few selected params
# while returning call dumps() method to convert to json

@app.get('/mongo/fruits')
def get_fruits_from_mongo():
    all_fruits = fruits_coll.find({}, {'_id': False})
    # dumps will convert bson to json
    return dumps(all_fruits), 200