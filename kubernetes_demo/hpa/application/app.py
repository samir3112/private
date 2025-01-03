from flask import Flask
import os

app = Flask(__name__)

@app.get("/greetings")
def get_grettings():
    greet_message = "Hi DevOps team , This is coming from container, Welcome to container world, looking at deployment"
    print(f"get_grettings() :: message is {greet_message}")
    return greet_message, 200