import os
import sys
import json

import requests

from slackclient import SlackClient

from flask import Flask, request, jsonify

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_token)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World", 

@app.route('/webhook', methods=['GET', 'POST'])
def verify():
    data = request.get_json()
    log(data)
    try:
    	if data["event"]["type"]=='member_joined_channel':
    		team_id = data["event"]["channel"]
    		return "ok", 200, send_greeting(team_id)
    except Exception,e: 
        print str(e)
    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

def send_greeting(team_id):
	sc.api_call(
		"chat.postMessage",
		channel=team_id,
		text="Hello from Python! :tada:"
		)

if __name__ == '__main__':
    app.run(debug=True)
