import os

from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


def send(number, message):
    options = {
        "body": message,
        "from_": os.environ["TWILIO_PHONE_NUMBER"],
        "to": "+{}".format(str(number)),
    }
    if os.environ["TWILIO_PROD_MODE"] == "TRUE":
        client.messages.create(**options)
    else:
        print(options)
