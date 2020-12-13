import socket

address = "192.168.240.8"
port = 20001
bufferSize = 1024

msgFromServer = "I am UDP SERVER"
byteToSend = str.encode(msgFromServer)

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((address,port))

print("berjaya create dan bind pada port:"+ str(port))

while True:
	bytes=s.recvfrom(bufferSize)
	message = bytes[0]
	addr = bytes[1]
	Cmsg="Message from Client:{}".format(message)
	ClientIP = "Client IP Address:{}".format(addr)

	print(Cmsg)
	print(ClientIP)

s.sendto(byteToSend, addr)

