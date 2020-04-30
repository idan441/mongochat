# Echo client program
import socket

HOST = '127.0.0.1' # The remote host, in my case I will be running the server on the same computer. 
PORT = 15000 # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	#Create a socket object, so that the computer can use it to connect to the server's socket. 
	#AF_INET = IPv4 address will be used by the socket for connection, SOCK_STREAM = socket working in TCP protocol. 

	s.connect((HOST, PORT)) #Try to connect to the socket in the desired hsot and port. This iwll work assuming the server.py file is running. 

	#Send a message through the socket to the server. The server is supposed to print that message. 
	s.sendall(b'Hello! This is a message from the client. ') 
	#send() functions sends the information once, and if it gets damaged then it is the applications proble. 
	#sendsall() makes the application send the data non-stop until all of it got completely to the application. 


	#Recieve data from the socket. The data is sent from the server. 
	data = s.recv(1024)

	print('Received: ', data)