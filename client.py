import socket

s = socket.socket()
host = '192.168.240.8'
port = 60000

s.connect((host,port))
s.send(b"Hello Server!!")


with open(b"received_file","wb") as f:
	print ("file opened")
	while True:
		print("Receiving data....")
		data = s.recv(1024)
		print("data=%s",(data))
		if not data:
			break
		#write data to file
		f.write(data)

f.close()
print("Successfully get file")
s.close()
print("coneection closed")
