import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8888

s.connect(('192.168.240.8',port))

data = s.recv(1024)

s.send(b'Hi,saya client.Thanks!')

print(data)

s.close()
