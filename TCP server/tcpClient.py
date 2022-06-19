import socket

HOST = '127.0.0.1'
PORT = 5050
#variables
header = 64
format = 'utf-8'
DISCONNECT_CODE = "q"
ADDR = (HOST, PORT)
#connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)

send("Allan John")
send("q")
