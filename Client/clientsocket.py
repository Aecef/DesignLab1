import socket

temp = 0.0
sock = None

def set_temp(new_temp):
    global temp
    temp = new_temp

def get_temp():
    global temp
    return temp

def set_sock(socket):
    global sock
    sock = socket

def get_sock():
    global sock
    return sock

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("172.20.10.12", 1242))

#s.connect(("192.168.0.196", 1242))

HEADERSIZE = 10
full_msg = ''
new_msg = True

def get_headersize():
    global HEADERSIZE
    return HEADERSIZE

def is_new_msg():
    global new_msg
    return new_msg

def set_is_new_msg(val):
    global new_msg
    new_msg = val


def temp_update():
    msg = get_sock().recv(16)
    global full_msg
    change_message = False
    full_msg = msg.decode("utf-8")[get_headersize():]
    if full_msg != '':
        set_temp(float(full_msg))


#        if is_new_msg():
#            #print(f"new message length: {msg[:HEADERSIZE]}")
#        msglen = int(msg[:get_headersize()])
#        set_is_new_msg(False)    
#    while not change_message:
#        full_msg += msg.decode("utf-8")
#        if len(full_msg) - get_headersize() == msglen:
#            #print("full msg recvd")
#            #print(full_msg[get_headersize():])
#            #set_temp(float(full_msg[get_headersize():]))
#            set_is_new_msg(True)
#            full_msg = ''
#            change_message = True
#    #print(get_temp())


