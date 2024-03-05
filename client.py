import socket
def send_file(conn, filename):
    with open(filename, 'rb') as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            data = file.read(1024)
def receive_file(conn, filename):
    with open(filename, 'wb') as file:
        data = conn.recv(1024)
        while data:
            file.write(data)
            data = conn.recv(1024)
def send_file_to_server():
    host = '10.12.201.75'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    filename = input("Enter the file that you would like to send:")
    # Send the steganography result file to the server
    client_socket.send(filename.encode('utf-8'))
    send_file(client_socket, filename)
    print(f"Steganography result sent to server: {filename}")

    client_socket.close()

def request_file_from_server():
    
    host = '192.168.166.74'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    filename = input("Enter the file that you would like to requested:")
    # Send the requested filename to the server
    client_socket.send(filename.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    if response == "File exists":
        # Receive and save the file on the client
        receive_file(client_socket, filename)
        print(f"File '{filename}' received from the server")
    else:
        print(f"File '{filename}' not found on the server")

    client_socket.close()

if __name__ == "__main__":
    request_file_from_server()

