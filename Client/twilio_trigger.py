from twilio.rest import Client

upper_limit = 33.0 #Upper Limit trigger for twilio in Celsius
lower_limit = 13.0 #Lower Limit trigger for twilio in Celsius

temp_moved_limit = False

account_sid = 'ACa62404846b80019bfc75dc5c3503db23'
auth_token = 'b2e808da58fc8417a884c56d565f7210'

twil_phone = '+19142923936'

client = Client(account_sid, auth_token)

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

def set_upper_limit(val):
    global upper_limit
    upper_limit = val

def set_lower_limit(val):
    global lower_limit
    lower_limit = val
    
def check_temp_above(temp):
    if temp >= get_upper_limit() and not get_temp_moved_limit():
        #add twilio call here
        set_temp_moved_limit(True)
    elif temp <= get_lower_limit() and not get_temp_moved_limit():
        #add twilio call here
        set_temp_moved_limit(True)
    else:
        set_temp_moved_limit(False)



