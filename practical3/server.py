import socket
import threading

HOST = '127.0.0.1' 
PORT = 3000

client_threads = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("Received:", message)
            
            broadcast(message)
            
        except Exception as e:
            print("Error:", e)
            break
    
    client_socket.close()

def broadcast(message):
    for client_thread in client_threads:
        client_socket = client_thread[0]
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            client_threads.remove(client_thread)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server is listening on {}:{}".format(HOST, PORT))

try:
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        
        client_threads.append((client_socket, client_thread))

except KeyboardInterrupt:
    print("Server shutting down.")
    for client_thread in client_threads:
        client_thread[0].close()
    server_socket.close()
