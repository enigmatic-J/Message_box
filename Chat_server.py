import socket, os, sys

RHOST = "192.168.1.156"
RPORT = 4444

sock = None
if sock is None:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
else:
	sock = sock

sock.bind((RHOST, RPORT))
print(f"Binding connection to {RHOST}:{RPORT}")

sock.listen(5)

while True:
	client, addr = sock.accept()
	print("Obtained connection from {}".format(addr))
	print("Wait for client response")

	for x in range(1,1000):
		returned_dat = client.recv(1024).decode()
		print("message from {} saying: {}".format(addr, returned_dat))
	
		# Message prompt
		message_to_client = input("Message> ")
		message_to_client = bytes(message_to_client, "utf-8")
	
		client.send(message_to_client)
		print("you've sent your message")
		print("Wait for client response")


