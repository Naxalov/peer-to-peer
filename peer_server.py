# peer_server.py

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Waiting for a peer to connect...")

conn, addr = server.accept()
print(f"Connected to {addr}")

while True:
    message = input("You: ")
    conn.sendall(message.encode())

    data = conn.recv(1024)
    if not data:
        break
    print("Peer:", data.decode())

conn.close()
