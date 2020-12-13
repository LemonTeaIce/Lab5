import socket 

port = 60000
s = socket.socket()
host = '192.168.240.8'
s.bind ((host, port))
s.listen(5)

print ("Server Listening..")

while True:
	conn, addr = s.accept()
	print ("Got connection from ", addr)
	data = conn.recv(1024)
	print("Server received", repr(data))

	filename = "text.txt"
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
		conn.send(l)
		print("Send",repr(l))
		l = f.read(1024)
	f.close()


	print("Done sending")

	#conn.send(b"thank for conect")
	conn.close()
