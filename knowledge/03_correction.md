# Some corrections about the former files and first project: 

## server 'host' property - 
As said, in order to create a socket object two basic properties need to be given - a host and a port. ( Along with defining the socket type etc... ) 
* port - is used to reffer to a specific socket, as a computer can run many of them. so when the message (also caleld data) reaches the compute it knows to send it to the right socket. 
* It is to note, that recofnizing the data uses 5 parameters: source IP, source port, destinatino IP, destination port and socket type. So the port is not the only things used recognize the data! 
* host - this one is important, as this is the IP address that the data should be sent to. Actually, the host is defined twice - on the client side and on the server side. 

### The value of host - 
The host is used to recognize the dstination the data should be sent to. 
* on the client side the host is the server's IP address. 
* on the server side the host is the client's IP address. 

**How should the host be defined on each side?** 
* When defining the socket's host on the client side, you should put the IP address of the server so it will know how to reach it. 
* When defining the socket's host on the server side, you need to define the IP addresses which the socket should listen to. 

Important - when defining the 'host' property in a server socket - then it will be used by the listen function to define the IP addresses it will be listening from! And only clients with such IP's can answer it! 

#### Deffining host = 127.0.0.1 on server side - 
A common mistake can be to set the 'host' on the server side as localhost 127.0.0.1 - in such case it will create a socket which can listen only to clients from this IP address! That means that only clients from the specific computer can connect to the server urnning on that computer! 
* In most of the client-server softwares it is bad! As foreginer computer can't login to the server. 
* IN some cases, there are softwares which server teh local computer only - and in such case defining the host to 127.0.0.1 can be a smart things, as it will block other computers from attacking or accessing the softwrae. Such an example can be MySQL database server which use ssocket to accept queries and to send answers back. This socket is also used when connecting from the local machine. In a case where you want only your machine to connect to the MySQL server then defining the host of the server to 127.0.0.1 is a good practice! 


# socket listen() function - 
The listen function is used to define the queue limit for incoming connections. 
When the client wished to connect to the server then it enters the incoming connections queue, and then the server **accepts** the connection. Only after that the client and server can write and read to each other. 


To accept connections, the following steps are performed: ( taken from - http://man7.org/linux/man-pages/man2/listen.2.html )

   1.  A socket is created with socket(2).

   2.  The socket is bound to a local address using bind(2), so that
       other sockets may be connect(2)ed to it.

   3.  A willingness to accept incoming connections and a queue
       limit for incoming connections are specified with listen().

   4.  Connections are accepted with accept(2).


**To sum -** when creating the socket and using the funciton listen(number) you need to define the amount of connections which can be waiting until their connection will be accepted. When accepting a connection the client's connections will be moved from the waiting queue defined by listen() function. If too many clietns are trying to connect to the server and their amount is getting bigger then the waiting queue size - the last ones will be refused for connection. ( That until the queue start to get smaller... ) 


