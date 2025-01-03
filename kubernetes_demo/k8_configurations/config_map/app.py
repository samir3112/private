import os
from flask import Flask

app = Flask(__name__)

who_to_greet = os.environ.get("who_to_greet_ev")
what_session = os.environ.get("session_ev")
session_duration = os.environ.get("duration_ev")
session_topics = os.environ.get("topics_ev")

@app.get("/session")
def session_info():
    greet_message = f"Hi {who_to_greet} , Welcome to {what_session} session.\n"
    devops_info = greet_message +  f"This course will last for {session_duration} months.The topics which will be covered are {session_topics}\n"
    return devops_info, 200

