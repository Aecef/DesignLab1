from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

def sendAlert(alert_message, uphone):
    message = client.messages.create(
        body = alert_message,
        from_= keys.from_phone,
        to = ("+" + uphone)
    )

sendAlert("function worked", '18156669066')