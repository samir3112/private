from flask import Flask
import time

app = Flask(__name__)
time.sleep(60)

# greeting  method
@app.get("/greetings")
def get_grettings():
    greet_message = "Hi DevOps team , This is coming from container, Welcome to container world, looking at deployment"
    print(f"get_grettings() :: message is {greet_message}")
    return greet_message, 200

# ready method for readiness probe
@app.get("/ready/check")
def get_ready():
    return "Pod is ready", 200