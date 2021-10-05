import socket

temp = 0
sock = None

def set_temp(new_temp):
    global temp
    temp = new_temp

def get_temp():
    return temp

def set_sock(socket):
    global sock
    sock = socket

def get_sock():
    return sock

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("172.20.10.12", 1242))

#s.connect(("192.168.0.196", 1242))

HEADERSIZE = 10
full_msg = ''
new_msg = True

def temp_update():
    msg = get_sock().recv(16)
    global HEADERSIZE
    global new_msg
    global full_msg

    if new_msg:
        #print(f"new message length: {msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg = False    
    full_msg += msg.decode("utf-8")
    if len(full_msg) - HEADERSIZE == msglen:
        #print("full msg recvd")
        print(full_msg[HEADERSIZE:])
        set_temp(float(full_msg[HEADERSIZE:]))
        test = get_temp()
        print(test)
        new_msg = True
        full_msg = ''
