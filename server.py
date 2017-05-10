from twilio.rest import Client
import os


access_token = os.environ['TWILIO_AUTH_TOKEN']
access_sid = os.environ['TWILIO_ACCOUNT_SID']


# Your Account SID from twilio.com/console
account_sid = access_sid
# Your Auth Token from twilio.com/console
auth_token  = access_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12018050073", 
    from_="+12013659575",
    body="Hello from Python!")

print(message.sid)