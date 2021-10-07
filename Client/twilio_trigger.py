from twilio.rest import Client

upper_limit = 33.0 #Upper Limit trigger for twilio in Celsius
lower_limit = 13.0 #Lower Limit trigger for twilio in Celsius

temp_moved_limit = False

target_phone = "18156669066"

twil_phone = '+19142923936'
client = None

def setClient(c):
    global client
    print(client)
    client = c
    print(client)


def get_client():
    global client
    return client

def sendAlert(alert_message, user_phone):
    message = client.messages.create(
        body = alert_message,
        from_= twil_phone,
        to = ("+" + user_phone)
    )

def set_temp_moved_limit(val):
    global temp_moved_limit
    temp_moved_limit = val

def get_temp_moved_limit():
    global temp_moved_limit
    return temp_moved_limit

def get_upper_limit():
    global upper_limit
    return upper_limit

def get_lower_limit():
    global lower_limit
    return lower_limit

def get_target_phone():
    global target_phone
    return target_phone

def set_target_phone(new_phone):
    global target_phone
    target_phone = new_phone

def set_upper_limit(val):
    global upper_limit
    upper_limit = val

def set_lower_limit(val):
    global lower_limit
    lower_limit = val
    
def has_temp_exceeded_limits(temp):
    if temp >= get_upper_limit() and get_temp_moved_limit():
        sendAlert("TEMPERATURE EXCEEDED THE UPPER LIMIT",get_target_phone())
        print("Twilio Sent:::::::")
        #add twilio call here
        set_temp_moved_limit(False)
    elif temp <= get_lower_limit() and get_temp_moved_limit():
        sendAlert("TEMPERATURE EXCEEDED THE LOWER LIMIT",get_target_phone())
        print("TWILIO SENT:::::")
        #add twilio call here
        set_temp_moved_limit(False)
    elif temp <= get_upper_limit() and temp >= get_lower_limit():
        set_temp_moved_limit(True)



