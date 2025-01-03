from flask import Flask
import urllib.request
import os

app = Flask(__name__)

auth_address = os.environ.get('AUTH_ADDRESS')
auth_svc_svc_host = os.environ.get('AUTH_SERVICE_SERVICE_HOST')

@app.post("/signup")
def signup():
    print("Inside user_api :: signup()")
    response = urllib.request.urlopen(f"http://{auth_address}/signup")
    return response.read(), 200

@app.post("/signup/svc")
def signupsvc():
    print("Inside user_api :: signupsvc()")
    response = urllib.request.urlopen(f"http://{auth_svc_svc_host}/signup")
    return response.read(), 200

