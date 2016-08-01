import socket


def Main():
	host = '192.168.1.63'
	port = 5000

	s = socket.socket()
	s.connect((host,port))

	message = raw_input('user-> ')
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		print 'client-> ' + str(data)
		message = raw_input('user-> ')
	s.close()

if __name__ == '__main__':
	Main()
