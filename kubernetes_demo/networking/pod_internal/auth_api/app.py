from flask import Flask

app = Flask(__name__)

@app.get("/signup")
def signup():
    print("Inside auth_api :: signup()")
    return "Sign Up Success", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)