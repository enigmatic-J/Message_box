import socket, os, sys, subprocess, platform, getpass

RHOST = "127.0.0.1"
RPORT = 4444

sock = None
if sock is None:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
else:
	sock = sock

sock.connect((RHOST, RPORT))
print("connection to {}:{} established".format(RHOST, RPORT))

def send(message):
	sock.send(message.encode())

while True:
	for x in range(1,1000):
		# Message prompt
		message_to_server = input("Message> ")
	
		send(message_to_server)
		print("you've sent your message")
		print("Wait for server response")
	
		recovery = sock.recv(1024).decode("utf-8")
		print("message from {}:{} saying: {}".format(RHOST,RPORT, recovery))
	
	
