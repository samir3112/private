from flask import Flask
import os

import threading

app = Flask(__name__)
lock = threading.Lock()

# greeting  method acquire lock and relese
@app.get("/greetings")
def get_grettings():
    lock.acquire()
    greet_message = "Hi DevOps team , This is coming from container, Welcome to container world, looking at deployment"
    print(f"get_grettings() :: message is {greet_message}")
    lock.release()
    return greet_message, 200

# this will cause container to exit , but k8 will restart it
@app.get("/error")
def get_error():
    print(" get_error() :: killing")
    os._exit(1)

# this method will acquire log and will try acquiring again and will get locked
# same lock is used in greetings method and if the process is locked then that method will not respond
@app.get("/lock")
def simulate_lock():
    lock.acquire()
    try:
        lock.acquire()
    finally:
        lock.release()
        
    lock.release()
    
    thread = threading.Thread(target=simulate_lock)
    thread.start()
    thread.join()
    return "Will never return for sure", 200