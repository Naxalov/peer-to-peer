# peer_client.py

import socket

HOST = 'localhost'  # Replace with server IP if remote
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to peer.")

while True:
    data = client.recv(1024)
    if not data:
        break
    print("Peer:", data.decode())

    message = input("You: ")
    client.sendall(message.encode())

client.close()
