import socket


def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()
	print 'Connection from : ' + str(addr)
	while True:
		data = c.recv(1024)
		if not data:
			break
		print 'client-> ' + str(data)
		data = raw_input('user-> ')
		c.send(data)
	c.close()

if __name__ == '__main__':
	Main()
