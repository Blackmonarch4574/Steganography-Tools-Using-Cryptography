# Client code

import socket
import os

# Initialize socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.157.74', 8000))

# Send file to server
file_name = input() # Change this to your file path

print("Sending file", file_name)

file_size = os.path.getsize(file_name)
client_socket.send(str(file_size).encode())
client_socket.send(file_name.encode())

with open(file_name, 'rb') as f:
    bytes_sent = 0
    while bytes_sent < file_size:
        data = f.read(1024)
        client_socket.send(data)
        bytes_sent += len(data)

print("File sent successfully")

# Close the connection
client_socket.close()