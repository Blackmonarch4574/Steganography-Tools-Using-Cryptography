import socket

def send_file(server_socket, filename):
    with open(filename, 'rb') as file:
        data = file.read(32768)
        while data:
            server_socket.send(data)
            data = file.read(32768)
            print('file sent ')

def receive_file(server_socket, filename):
    with open(filename, 'wb') as file:
        data = server_socket.recv(32768)
        while data:
            file.write(data)
            data = server_socket.recv(32768)
    print('file recieved ')

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.166.74', 8888))

    while True:
        print("1. Request File from Server")
        print("2. Send File to Server")
        print("3. Close Connection")
        choice = input("Enter your choice")
        client_socket.send(choice.encode())

        if choice == '1':
            filename = input("Enter the filename to request: ")
            client_socket.send(filename.encode())
            receive_file(client_socket, filename)
            # print(client_socket.recv(1024).decode())
            

        elif choice == '3':
            filename = input("Enter the filename to send: ")
            client_socket.send(filename.encode())
            send_file(client_socket, filename)

        elif choice == '2':
            print("Closing connection.")
            client_socket.close()
            break

if __name__ == "__main__":
    main()