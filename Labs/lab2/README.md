# Lab #2: TCP Client Socket 
Please read this README file before class and use this as a reference during the lab session. 

In this lab, students will learn to create a TCP client socket that sends and receives messages to-from a 
server socket. Please read the instructions provided in this README file carefully. 

In this lab you are provided with the following files:

   1. server.py -- Please do not modify this file. This is a server used as an example for this lab. You will
      create your own server in lab3
   2. client.py -- You must implement the methods in this file for this lab
   3. clienthelper.py -- the client helper processes requests and responses to/from the server   

## Useful hints to guide your implementation in client.py  

### How to create a client socket. 

1. In order to create a client socket, you, first,  need to import the socket library builtin in the standad Python libraries.
The socket library provides all the low level functions needed.
2. The following line of code creates a client socket. So, you can use that socket to call 
methods such as connect(), send(), recv()...
```python
# TCP client socket
import socket
# AF_INET is the connection domain. In this case, IPv4
# SOCK_STREAM is the type of connection. STREAM means that that socket will use a TCP based connection
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
```  
3. Connect to a well know server. A well know server is a server which IP address, port or hostname is well know by the 
client. In this lab. you can assume that your client will connect to a server via Local Area Network (LAN), and the IP 
address and port of the server will be provided by the instructor. 
```python
# Connects to a server socket running at 127.0.0.1/12000
# In your lab, you need to provide error handling mechanisms
# to handle connection errors (i.e server is not running)
server_ip_address = "127.0.0.1"
server_port = 12000
clientsocket.connect((server_ip_address, server_port))
```
4. Python client sockets provide functions to send and receive raw data to/from other sockets. The data sent must be 
serialized and the data received must be deserialized because the data must be transmitted using
the TCP protocol as a stream of bytes. In order to accomplish this we can use the Python library Pickle 
```python
import pickle 
alice = "Alice"
# stream of bytes ready to be send
alice_serialized = pickle.dump(alice)
# after received deserializes the data from bytes to string  
alice_deserialized = pickle.loads(alice_serialized) 

```
Note that in the above example we were not sending or receiving data. We were just serializing data (ready to be sent) 
and deserializing data (assume the serialized data was received)

When a server accepts a connection, it assigns a client id to the client. It must be serialized by the server (already
implemented on the server side in this lab), and it also needs to be deserialized by the client once it is received 
(must be implemented in this lab)


6. How do we know if the server received the data that the client just sent?. The server acknowledges that the data was 
received. Note that no error in sending the data does not mean that the server received the data. 
(i,e server closed the connection before receiving the data). That is why the server must acknowledge that the
data was received. In this lab, the sample server given to students, sends to the client, the integer 1 to acknowledge that the 
data was received 

### How to keep the client alive waiting for server responses?
This step is already implemented for you in the test.py file

Take into consideration that a client needs to be listening all the time for server responses even if the client did not 
send a request. Otherwise, the client program would be terminated and therefore, its connection to the server would 
be automatically closed by the client program. How can we implement the client to be in listening mode all the time? 
We need to set a forever loop and break it if the data was corrupted or upon receiving the data, it is empty. 

```python
# client keeps listening for more data
while True: 
   data = client.receive(max_all_buffer) # blocking method. 
   if not data: 
       break
   # process the data here.
```
### The Client Helper 

The responsibilities of the client are only to connect to the server and keep the connection alive until the
socket is closed. 

The ClientHelper object helps the client to process all the request/responses to/from the server. That way, we can
reuse the Client class in other systems, and we can scale better the system with different functionalities.  

## Your Job in this Lab

1. Implement all the methods marked as TODO in your client.py file

2. Implement all the methods marked as TODO in your clienthelper.py file

3. Open a command line windows and type the following command to run the server (provided in this lab): 
   
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


