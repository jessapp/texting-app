from twilio.rest import Client

from random import randint

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


    facts = {1: "The panda's scientific name is Ailuropoda melanolecua, which means 'black and white cat foot.'",
             2: "Pandas walk with their front paws turned inward.",
             3: "The Chinese word for panda is 'xiongmao,' which means 'bear cat.'",
             4: "Pandas like to eat bamboo because they have no umami taste receptors, so meat tastes bland to them.",
             5: "Adult pandas have to eat as much as 80 pounds of bamboo every day to meet their nutritional needs.",
             6: "Pandas have lived on earth for 2 to 3 million years."}

    random_num = randint(1,6)

    message = client.messages.create(
        to="+1" + phone_number, 
        from_="+12013659575",
        body=facts[random_num])

    print(message.sid)

    return redirect("/")

if __name__ == '__main__':

    app.run()