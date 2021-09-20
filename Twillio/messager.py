from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body = "Alec does a test sms to make sure it works ;)",
    from_=keys.from_phone,
    to=keys.target_phone
)

print(message.body)