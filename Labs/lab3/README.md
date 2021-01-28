# LAB #3: TCP Server Socket. 
Please read this README file because it contains many hints and references that will help students in completing this lab

In this lab, students will create a TCP Server socket object. This server will only support one client at a time
and will handle requests made by such clients. Note that real servers support multiple connections pipelined. In next lab, 
students will modify this server to create a server that supports multiple connections (like the real ones)

In this lab you are provided with the following files:

   1. server.py -- students must implement this file
   2. client.py -- copy and paste from your lab2 implementation
   3. clienthelper.py -- copy and paste from your lab 2 implementation

## Useful hints to follow in this lab 

### How to create a TCP server socket. 

1. In order to create a server socket, first you need to import the socket library builtin in the standard Python libraries.
The socket library provides all the low level functions needed.

2. The following line of code creates a server socket. So, you can use that socket to call 
methods such as bind(), listen(), accept(), send(), recv()...

```python
import socket 
# creates the server socket 
# AF_INET refers to the address family ipv4
# SOCK_STREAM parameter tells the socket to use the TCP protocol (reliable connection oriented.)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

3. Binding the server: once the server socket is created, it needs to be bind to a ip address and port in order to 
start listening for other clients. 

Note that binding is optional in a client socket. However, it is mandatory in a server socket before putting it to 
listen for other clients connection requests. The reason is simple, the server needs to be bind to a well know 
IP address and port so other clients can use those parameters to create a successful connection with that server. 

Below is an example that binds and puts to listen a server socket in a specific IP address and port. Note that the
native bind method from the server socket takes as a parameter the host and port enclosed in a tuple. 

```python
host = "127.0.0.1"
port = 12000
# will keep only 10 clients waiting in the server queue. 
# Additional requests when queue is full will be drooped. 
MAX_NUM_CONN = 10 
# bind ip address and port
serversocket.bind((host, port)) # (host, port) are passed as a parameter in a tuple. 
serversocket.listen(NAX_NUM_CONN) # server starts listening for client connections. 
```

4. Clients connections: once a client is accepted by the server, the server will create a TCP persistent connection
with that client. in this lab the connection you will create is not pipelined (one client at a time). 

When multiple clients are connected. How a client handler knows to which client send the data if the 
low level send() method does not provide a option to define the client recipient? Here is where your
CSC415 knowledge comes in handy. The client handler is a forked process from the client. This operation is 
implemented at the low level in the method accept() from the server socket. Both of them (client 
and its client handler) share the same client id which basically is the pid of the process. Therefore, the client
handler related to a client process knows exactly where to send the message based on the pid. This is already 
implemented by the Python sockets library. So, you don't need to worry about this. But it's good to know how
things work behind the scenes in order to see the whole picture. 

Note that in order to keep the server accepting clients as they connect, you must put the following code inside 
a loop, and break the loop if there is an error with the accept clients process on the server side. Also note
that it is imperative that the server handles occurring exceptions properly. So, when an exception occurs, it must
be logged and the server must continue its operations as normal
 

```python
# server accepts a client trying to connect
# clienthandler is the handler of the client socket in server side. 
# it will share messages on behalf of the server with the original client socket. 
# addr contains server ip/port and client id assigned to the client
clienthandler, addr = serversocket.accept() # this is a blocking method. 
server_ip = addr[0]
client_id = addr[1] 
```

5. The client handler has the capabilities of sending and receiving data. This data is only send/received to/from 
the parent client. Client handler are isolated from other client handlers in the same system. This means that 
any operation done by a specific client handler does not interfere with other client handler or other clients 
for that matter. 

In the following example, the client handler of client X is sending to that client the client id assigned by the server  

```python
import pickle 
data = {'clientid': client_id} 
serialized_data = pickle.dumps(data) 
clienthandler.send(serialized_data) # data sent to the client from its handler
```

6. The receive data process is handled by the client handler (not the server)

```python
MAX_ALLOC_MEM = 4096
# server receives data
data_from_client = clienthandler.recv(MAX_ALLOC_MEM) 
# deserializes the data received
serialized_data = pickle.loads(data_from_client) 
# do something with the data. 
```


## Important Notes

1. The server must handle errors and exceptions properly. 
2. Server must not be stopped when a exception occurs. Inform the user about the error instead 
in server console when a exception occurs, and continue the server operations as normal 
3. In this lab, you will learn to handle only one client at a time. In lab 4, you'll learn how to
handle multiple clients connections pipelined  


## Your Job in this Lab

1. Implement all the methods marked as TODO in your server.py file

3. Open a command line windows and type the following command to run your server: 
   
   ```shell script
      python3 server.py
   ``` 
   
   If there are no errors, you should see the following output:
    
   ```shell script
      Listening at 127.0.0.1/12000 
   ``` 
   Note that the ip and port may be different in your case if you modified the server parameters. 

4. Open a new command line windows (don't kill the one with the server) and type the following command: 
    
    ```shell script
      python3 client.py
    ``` 
   
   In order to pass this lab, your screen (on the client side) should show: 
   
    ```shell script
      {'clientid': 60644} has successfully connected to 127.0.0.1/12000
      Data acknowledged by server and you passed the test
    ``` 
   
   Note that in your case, your client id will be different, and the ip and port from the server may also be different 
   if you modified the server parameters. I recommend not to modify the code on server.py
   
5. Take a look at your server windows where you run the server, you should see similar output as the one below
with your student info:

    ```shell script
       Listening at 127.0.0.1/12000
       Connected: Student: Alice Brown, Github Username: abrown, sid: 123456789
    ```


