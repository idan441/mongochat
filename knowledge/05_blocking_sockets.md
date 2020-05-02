#What is a blocking socket? 
Generally, a TCP protocol socket is a "blocking" socket. That means that when sending a command to this socket, the program "freezes" until it responds. So for example, when trying to accept a conneciton the programm will stop until the socket will recieve an answer, whether it is ye or ney. 

This can be problematic with chat applications, which needs to handle many connections, as when doing one single command on a socket will "freeze" the application, preventing the server and other clients from sending or reading actions. For example, assuming a server is using socket.accept() to accept a new client, the server program will freeze and will not be able to recieve any messag efrom the otehr client. Also it won't be possible to send messages to the clients meanwhile. 

The solution is using "non-blocking socket" which is an option defiend at the socket creation. This de-couples the socket actions (functions) from the program. THis will make the program to keep running, while accepting new connections, writing to socket and reading ot sockets. So for example, it will be possible taht a client will write to the one socket, while the program reads another socket - or even the socket which is being written on the same time! 

Refferences - 
https://www.scottklement.com/rpg/socktut/nonblocking.html