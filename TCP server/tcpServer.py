import socket
import threading
HOST = '127.0.0.1'
PORT = 5050
#variables
header = 64
format = 'utf-8'
DISCONNECT_CODE = "q"
#binding
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
#Setting up client-server data exchanging
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected= True
    while connected:
        msg_length= conn.recv(header).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == DISCONNECT_CODE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()
#setting up client -server connection
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()