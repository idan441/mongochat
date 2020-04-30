# The socketkind object - 
When accepting a connection via socket, then it returns a socketkind object. Also in python it returns another object which is a list (tuple in python) with the IP and port of the remote socket. 

By looking at the example at 01_basic - 
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	#AF_INET = IPv4, SOCK_STREAM = TCP protocol. 

	sock.bind((HOST, PORT)) 
	sock.listen(3) #listen() will make the system to accept connections to the socket. The numeric argument specifies the amount of connections allowed at the waiting queue until being accepted by the accept() function. 
	print("running server in host {} port {}".format(HOST, PORT))


	conn, addr = sock.accept() # accept() is a functions which accepts a connectino from a client. It returns another socker object and the IP address of the other side. conn = a socket with an open connections with the client, addr = the IP (IPv4) address of the client. 
	print(conn)
	print(addr)
```
***The above text is taken from the file server.py which I added two command of printing. )***

The output which will be printed is - (After connecting with a client from the server. ) 
```python
running server in host  port 15000
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 15000), raddr=('127.0.0.1', 59830)>
('127.0.0.1', 59830)
connect create from IP address:  ('127.0.0.1', 59830)
```


## How many socket there are in a program? 
* The new socketkind object is a socket object which represent the connection between the client and server. 
* FOR EVERY CONNECTION BETWEEN THE CLIENT AND THE SERVER - THERE WILL BE A SOCKET OBJECT. 
* So for example, a server with 2 clients will have 3 socket object: one which is accepting new connections and two socket which each of them is a connection with a client. ( 2 socket = 2 clients. ) 


**In other words** - 
* One socket is created at the server which accepts new connections, it is a queue of connection which needs to be created. ( This is the part of bind() function which creates the socket and listen() functions which defines the waiting queue. ) 
* Each of these connections should be later represented by an independent socket between the client and the server. This is done by the accept() function which returns a socket object which is the connection between the client and a server. 

To sum up - a socket object can be used for many cases - 
* As a server socket to accept new connections. These connection will be in a waiting queue. 
* As a connection between a client and a server - this sockets can be created in two ways - 
	* From the server side - by accepting new connections from the socket which is the waiting queue. 
	* From the client side - it is created manually by code lines, and it connect to the server socket, which puts the connection in waiting and later created a new socket-kind. 