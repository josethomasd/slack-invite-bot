import os
import sys
import json
import time
import requests

from slackclient import SlackClient

from flask import Flask, request, jsonify
import pickle

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(SLACK_BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World", 

@app.route('/webhook', methods=['GET', 'POST'])
def verify():
    data = request.get_json()
    log(data)
    try:
    	if((data["event"]["type"]=='member_joined_channel') & (data["event"]["channel"]=="C69KJGBEJ")):
    		try:
    			pickle_off = open("Emp.pickle","rb")
    		except Exception as f:
    			emp = "xyz"
    			pickling_on = open("Emp.pickle","wb")
    			pickle.dump(emp, pickling_on)
    			pickling_on.close()
    			pickle_off = open("Emp.pickle","rb")
    			log("Pickle fail")
    		emp = pickle.load(pickle_off)
    		event_id = data["event_id"]
    		# team_id = data["event"]["channel"]
    		pickling_on = open("Emp.pickle","wb")
    		pickle.dump(event_id, pickling_on)
    		pickling_on.close()
    		log('Old Event id: '+ emp)
    		log('Current Event id:' + event_id) 		
    		if(event_id!=emp):
    			return "ok", 200, send_greeting(team_id)
    except Exception,e: 
        print str(e)
    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()

def send_greeting(team_id):
	image_url = "https://i.imgur.com/kCK6yK1.png"
	attachments = attachments = [{"title": "",
                              "image_url": image_url}]
	sc.api_call(
		"chat.postMessage",
		channel=team_id,
		text="Welcome! :tada:",
		attachments=attachments
		)
	# time.sleep(10)

if __name__ == '__main__':
    app.run(debug=True)
