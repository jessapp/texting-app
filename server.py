from twilio.rest import Client

import os

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session)

from flask_debugtoolbar import DebugToolbarExtension

import json

app = Flask(__name__)

app.secret_key = "ks3sn4kynsna87d6f5"

app.jinja_env.undefined = StrictUndefined


access_token = os.environ['TWILIO_AUTH_TOKEN']
access_sid = os.environ['TWILIO_ACCOUNT_SID']


account_sid = access_sid
auth_token  = access_token

client = Client(account_sid, auth_token)

@app.route('/', methods=["GET"])
def index():
    """Homepage"""

    return render_template("body.html")

@app.route('/', methods=["POST"])
def index_process():
    """Execute text message"""

    phone_number = request.form.get("phone")

    message = client.messages.create(
        to="+1" + phone_number, 
        from_="+12013659575",
        body="Hello from Python!")

    print(message.sid)

    return redirect("/")

if __name__ == '__main__':

    app.run()