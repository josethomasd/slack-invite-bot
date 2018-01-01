import os
import sys
import json

import requests

from flask import Flask, request, jsonify

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route('/webhook', methods=['GET', 'POST'])
def verify():
    data = request.get_json()
    log(data)
    if data["challenge"]:
    	challenge = data["challenge"]
    	return jsonify(
            challenge = challenge
        )
    return "ok", 200
def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
