import socket #This will import socket objects class which can create, read, write to sockets. 


HOST =''
PORT = 15000
RECV_BUFFER = 4096 



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	#AF_INET = IPv4, SOCK_STREAM = TCP protocol. 

	sock.bind((HOST, PORT)) 
	sock.listen(3) #listen() will make the system to accept connections to the socket. The numeric argument specifies the amount of connections allowed at the waiting queue until being accepted by the accept() function. 
	print("running server in host {} port {}".format(HOST, PORT))


	conn, addr = sock.accept() # accept() is a functions which accepts a connectino from a client. It returns another socker object and the IP address of the other side. conn = a socket with an open connections with the client, addr = the IP (IPv4) address of the client. 
	print(conn)
	print(addr)

	print('connect create from IP address: ', addr) #Prints the IPv4 address of the client. 

	conn2, addr = sock.accept() # accept() is a functions which accepts a connectino from a client. It returns another socker object and the IP address of the other side. conn = a socket with an open connections with the client, addr = the IP (IPv4) address of the client. 
	print(conn)
	print(addr)

	print('connect create from IP address: ', addr) #Prints the IPv4 address of the client. 

	#Now, read and sned data from the socket connections as long as it is active. 
	with conn: 
		#Again, when using "with" statement then on any case, no matter what, at the stop of execution of this program - the conn object will be destroyed. 
		while True: #As long as the connection is active with the client. 
			data = conn.recv(1024)
			data2 = conn2.recv(1024)
			print(data)
			print(data)

			# if not data: 
			# 	print("data recieved is empty - exiting program")
			# 	break
			

			conn.sendall(b'hello from server') 
			# b in the beggining means to translate the string to binary mode. 
			# The socket created at the beggining of the script is represented as a file in the OS, and the file created in binary mode. Therefore, all accepted and sent messages needs to be in binary format. 
			# In the real project, it should be checked how to use no binary mode... 



#Refferences - 
	
	# Usage of "with" in the above python code - 
	# "With" in Python - usage of with statement is a good habit here - 
	# The "with" statement is creating an object, allows manipulating it in the indented block of the "with" . 
	# The most important part is that after the block is executed the object is deleted/closed/finished and not keep staying. 
	# Even when there is an exception / error wish exists the program - the object defined with "with" is being destroyed. This can cme useful when using files for example, so that they will be closed even when having an error. In this case a socket is defiend and after the code run, or when there is an error, the socket will be destroyed. ( The socket is in system level, so if it won't be destroyed by the program the socket will stay open... ) 

	# The difference between "try" and "with" : 
	# When try is having an exception (error) then it will stop the execution of the code, but object defiend won't be destroyed. Normally the objects defined are in the python program level so the stopping of the executen frees the memory adn resource. However, if the object is defined by system-level, so it will keep staying and taking resources until the systme will be restarted or that the item will be destroyed manually by an admin. 
	# However, if the object is defined with "with" then the stop of execution will work different than the "try" . The python program will destroy the object defiend in the "with" statement and just then will throw the output which will stop the program for running. WHich means that before the python program will exit - the object will be destroyed and the resource will be freed! 

	# So why using "with" here? 
	#"with" is used here to create the socket object. Inside the "with" block  all connection functions will be held. After the execution, or whether there is an exception - the socket object will be destroyed. ( And the socket won't stay open in the system level, while python stopped working. ) 


#Information was taken from the official documentary of Python - 
	# https://docs.python.org/3/library/socket.html