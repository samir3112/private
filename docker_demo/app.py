from flask import Flask

app = Flask(__name__)

who_to_greet = "DevOps team"

@app.get("/")
def get_greetings():
    greet_message = f"Hi {who_to_greet} , This is coming from container, Welcome to container world, again"
    return greet_message, 200