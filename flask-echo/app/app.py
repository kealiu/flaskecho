import os
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

SERVER_NAME=os.environ.get('SERVER_NAME', 'DEFAULT_NAME')

UPSTREAM=os.environ.get('UPSTREAM')

@app.route('/')
def hello_world():
    messages = []
    if UPSTREAM:
        reply=requests.get(UPSTREAM+"?msg="+SERVER_NAME)
        messages.append(reply.text)

    msg = "Requested by "+request.args.get("msg", "_")+" , serviced by "+SERVER_NAME
    messages.append(msg)
    return jsonify(message=messages)
