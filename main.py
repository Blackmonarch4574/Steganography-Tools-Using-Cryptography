import socket
def send_file(conn, filename):
    with open(filename, 'rb') as file:
        data = file.read(32768)
        while data:
            conn.send(data)
            data = file.read(32768)
def receive_file(server_socket, filename):
    with open(filename, 'wb') as file:
        data = server_socket.recv(32768)
        while data:
            file.write(data)
            data = server_socket.recv(32768)
    print('file recieved ')

def send_file_to_server():
    host = '192.168.166.74'
    port = 8888
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    while True:
        print("Type 3 to send file in the server")
        print("Type 4 Close Connection")
        choice = input("Enter Your Choice")
        client_socket.send(choice.encode())
    # Send the steganography result file to the server
        if choice == '3':
            filename = input("Enter the file name to send")
            client_socket.send(filename.encode('utf-8'))
            send_file(client_socket, filename)
            print(f"Steganography result sent to server: {filename}")
        elif choice == '4':
            print("Closing connection.")
            client_socket.close()
            break


def list_files(sock):
    #sock.send("LIST".encode('utf-8'))
    files = sock.recv(1024).decode('utf-8')
    print("Files in the server:")
    print(files)

def request_file_from_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.166.74', 8888))

    while True:
        print("Type 1 List of files in the server")
        print("Type 2 Request File from Server")
        print("Type 4 Close Connection")
        choice = input("Enter your choice")
        client_socket.send(choice.encode())
        if choice == '1':
            list_files(client_socket)
        elif choice == '2':
            filename = input("Enter the filename to request: ")
            client_socket.send(filename.encode())
            receive_file(client_socket, filename)
        elif choice == '3':
            print("Closing connection.")
            client_socket.close()