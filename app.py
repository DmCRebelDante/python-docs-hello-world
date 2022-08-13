from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, It's sue time, everyone needs a lawyer!"

