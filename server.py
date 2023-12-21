import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname()) 
PORT = 5050
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MSG = "!disconnected"
FORMAT = 'utf-8'
STR = " hello world"

def recv_msg(conn):
    msg_len = conn.recv(64).decode(FORMAT)
    if msg_len:
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(FORMAT)
        return msg

def send_msg(conn, msg):
    msg = msg.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (64 - len(send_len))
    conn.send(send_len)
    conn.send(msg)

def handle_client(conn, addr):
    global STR
    print(f"[New Connection] {addr} connected.")
    connected = True
    try:
        while connected:
            name = socket.gethostbyaddr(addr[0])
            msg = recv_msg(conn)
            if msg == DISCONNECT_MSG:
                connected = False
                print(f"[Connection Closed] {addr}")
            else:
                print(f"[{name[0]}]: {msg}")
                STR = msg
            if STR != " ": 
                send_msg(conn, STR)
                STR = " "
    except Exception as e:
        print(f"[Error] {addr}: {e}")
    finally:
        conn.close()

def start():
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.active_count() - 1}")

if __name__ == "__main__":
    print("Server is starting...")
    start()