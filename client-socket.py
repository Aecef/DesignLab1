import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.20.10.12", 1242))

#s.connect(("192.168.0.196", 1242))

full_msg = ''
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        #print(f"new message length: {msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg = False    
    full_msg += msg.decode("utf-8")
    if len(full_msg) - HEADERSIZE == msglen:
        #print("full msg recvd")
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ''