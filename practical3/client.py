import socket
import threading


HOST = '127.0.0.1' 
PORT = 3000 

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print("Received:", message)
        except:
            print("Connection closed.")
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

try:
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    client_socket.close()
