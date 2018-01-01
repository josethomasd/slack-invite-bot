import os
import sys
import json

import time

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route('/webhook', methods=['GET'])
def verify():
    return "OK", 200


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
