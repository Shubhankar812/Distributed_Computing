import socket as skt

s = skt.socket()
print("Socket created !")


port = 12345

s.bind(('',port))

s.listen(5)

while True :
    c,addr = s.accept()
    print('Got a new connection request')
    c.send('Thanks for connecting'.encode())
    c.close()
    break