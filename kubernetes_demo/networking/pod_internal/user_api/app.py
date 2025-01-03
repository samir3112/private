from flask import Flask
import urllib.request
import os

app = Flask(__name__)

auth_address = os.environ.get('AUTH_ADDRESS')

@app.post("/signup")
def signup():
    print("Inside user_api :: signup()")
    response = urllib.request.urlopen(f"http://{auth_address}/signup")
    return response.read(), 200

