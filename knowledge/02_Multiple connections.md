# How does multiple connections work in a socket? 
When a client connect ot a server via a socket, then a connection is made. 

The server knows the identity of the client by its IP address and port. 
In order to send a message to a specific client you need to reffer the socket with the IP address and port. 

## What happens when two clients are connecting simoultaneously? 
When one client connect ot the server - then the server obviously will send the message to the client according to it's IP address and port. 
If there are multiple connections, then the server will reffer to each client with it's unique IP address and port. 

**And what if there are two clients from the same machine?** In such case, the server will connect to the client in a different port. ( Assigned randomly. ) By doing that, the server will create two different identities for the clients ont he same computer - they will both have the same IP address - but a different port! This will be done automatically. 
This will apply for not only 2 but more clients! 

## How is the socket identified? 
The socket is identified by 5 properties - {SRC-IP, SRC-PORT, DEST-IP, DEST-PORT, PROTOCOL}
As said before, if using the same computer to login to the same socket then a different port will be assigned. ( As all other 5 properties are the same, and the 4 of them are permenant - so only **port** can be changed and still route the same computer. ) 

### Can two sockets be using the same port? 
As said above, the socket client-server connection is defined by 5 parameters, and in order to make sure that no two clients will use the smae identity - they must have at least 1 different parameter between them. 

So given two clients connect to a socket on a server - they must have different IP address or PORT on the server or client. (the port on their computer also count- if both clients use a different port then it is fine! ) And when the clients are running form the same computer and ports - then the server will assign one of them a rnadom port which is different. This will give them a different port - which makes sure the identities differ. 

**But what about runnig multiple socket on the server or client running on the same port?** In such case the answer can be yes it is possible **or** no it isn't. 
* If the sockets are having different properties - it is possible as the server can distinguish between the connection. For example - running two socket on the same server but different socket type! ( TCP or UDP for example. ) In such case both socket will have the smae IP address and port - but the protocol will be different. In such case, the server will recieve the data and will check the protocol of the message - and will traffic the message to the right socket. ( The message sent in each protocol has a different structure - thus allowing the server to distinguish between the sockets. ) 
* However, if the running server has to run the sockets on the same port and **in the same protcol** then it is impossibe! In such case the ip address is the same, the port is port is the same - and also the protocol. Messages recieved from both protocols will have the same structure - and the server won't be able to know which message to send to which socket. 
*Also note - there can be special protocols which can differ between the messages and allow multiple socket on the same port. In such case, one socket or applicaiton will recieve the message, analyze it - and then will sned it to the right application. But this is catchy and not what I am working on right now... 

That means that the same computer cna connect to a server up to 64 thousand conncetion! ( The maximum number of ports in a computer, as this day. ) This is assuming all client are from the same computer and and each time a sifferent port is assigned. 




## Refferences - 
https://stackoverflow.com/questions/3329641/how-do-multiple-clients-connect-simultaneously-to-one-port-say-80-on-a-server