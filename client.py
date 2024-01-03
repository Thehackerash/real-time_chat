import socket

PORT = 18257
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disconnected"
SERVER_URL = 'tcp://0.tcp.in.ngrok.io:18257'

# Extract host and port from the URL
server_url_parts = SERVER_URL.split(':')
SERVER_HOST = server_url_parts[1][2:]  # Remove '//' from the beginning
SERVER_PORT = int(server_url_parts[2])

ADDR = (SERVER_HOST, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
name = socket.gethostname()

def recv_msg(conn):
    msg_len = conn.recv(64).decode(FORMAT)
    if msg_len:
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(FORMAT)
        return msg

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (64 - len(send_len))
    client.send(send_len)
    client.send(message)

if __name__ == "__main__":
    print("Client is starting...")
    name = socket.gethostname()
    send_msg(name)
    while True:
        msg = input(f"{name}: ")
        send_msg(msg)
        print(recv_msg(client))
