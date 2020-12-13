import socket

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
SAPort = ("192.168.240.8",20001)
bufferSize = 1024

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

c.sendto(bytesToSend, SAPort)
msgFromServer = c.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
