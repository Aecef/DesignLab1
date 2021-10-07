
upper_limit = 33.0 #Upper Limit trigger for twilio in Celsius
lower_limit = 13.0 #Lower Limit trigger for twilio in Celsius

temp_moved_limit = False

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



