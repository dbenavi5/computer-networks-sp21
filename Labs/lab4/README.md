# Lab #4: Pipelined Connections, Threading and Locking on Server Side

In this lab, students will modify server.py from lab 3 to support multiple clients with pipelined connections. In
addition, students will implement the ClientHandler class in clienthandler.py. 

The ClientHandler object is the one that receives and processes the requests from the parent client. In lab3, 
students handled this situation with the method process_request(...) implemented on the server.py file which 
handled one request at a time. However, now our server must support pipelined connections (asynchronous connections) to support and serve
multiple clients that may send requests at the same time. Due to this, we must reduce the responsibilities of the server
and giving all the processing responsibilities to the handler objects. 

The main advantage of this new server's design, apart from the obvious improving on the general system performance, 
is that the Server object can be reused again in other systems without interfering in the modular implementations 
of that specific system. Real world servers support multiple TCP pipelined connections like the one students are 
implementing in this lab. 

For more information about pipelined connections/transmissions please refer to the transport layer slides, or class lectures
about that topic

In this lab you are provided with the following files:

   1. server.py -- students must implement (or delete) the methods marked as TODO
   2. client.py -- copy and paste from your lab2 implementation
   3. clienthelper.py -- copy and paste from your lab 2 implementation
   4. clienthandler.py -- students must implement the methods marked as TODO

First of all, lets see what we have done so far: 

```python
# basic example of accepting a client in server side.
# this example assumes the server is already listening
# assume this function exists

class Server:

# most of the code has been omitted to focus on the topic

def process_request (self, clienthandler):
    # do something with the clienthandler.
    pass

def accept_clients():
    while True:
        clienthandler, addr = serversocket.accept() 
        request = # ....
        self.process_request(clienthandler, request) 
```
The above code is blocking the main thread in the server side when a client is accepted because the 
handler will be calling the recv() method waiting for client messages. Therefore, only one 
client can use the server at a time. If another client wants to use the server, it needs to wait until the
first client disconnects from the server. Obviously, our server must support multiple and simultaneous
client's connections to meet the basic requirements enforced by modern apps.  

### How can we fix it? 

In order to fix this, we need to thread clients and lock some operations from those threads (e.g print). There are many 
ways to create threads in Python. The following code shows one of the easiest way of implementing that functionality. 

```python
# basic example of accepting a client in server side.
# this example assumes the server is already listening. 
from threading import Thread 

def handler(self, clienthandler, addr):
    # do something with the clienthandler (i.e send data to the client)
    pass

def accept_clients():
    while True:
        clientsocket, addr = serversocket.accept()
        Thread(target=self.handler, args=(clientsocket, addr)).start() # client thread started   
```

The above code creates a thread of the handler method that is handling a specific client. That way, clients
won't block the main thread, and that way the server can handle multiple requests without 
blocking the main thead. 

But, is this the ideal situation in a server? Not at all. The Server object, by itself, cannot handle all 
the responsibilities as the system scales. We must split those responsibilities with ClientHandler objects
to reduce the server overload.    

## The ClientHandler Class 

The client handler class provides a clean and scalable way to deal with multiple clients in our client-server architecture.
using TCP. It provides great advantages such as encapsulating data processing separately from the server class. 
Therefore, we can reuse our server class in other applications. The following is an example of a ClientHandler class

```python
import pickle
class ClientHandler:
 
    def __init__(self, server_instance, clientsocket, addr):
          # the server instance is passed as self by the server. 
          # so the class has access to all the server methods in running time
          # code omitted
          self.server_ip = addr[0]
          self.client_id = addr[1]
          self.server = server_instance
          self.handler = clientsocket
          
   
    def process_requests(self):
         pass # code omitted
         
```

### How do we thread an object of the ClientHandler class in the server?

We use the handler method on the server to create a ClientHandler object and start the object

The handler(..) method that creates the ClientHandler object is threaded inside the accepts_clients(...). Note that 
we are threading the method creating the object rather than the object itself. 

```python
# basic example of accepting a client in server side.
# this example assumes the server is already listening

from clienthandler import ClientHandler
from threading import Thread

def handler(self, clientsocket, addr):
    clienthandler = ClientHandler(self, clientsocket,addr)
    # some code omitted here 
    clienthandler.run()
   
def accept_clients():
    while True:
        clienthandler, addr = serversocket.accept() 
        # create new client thread. 
        Thread(target=handler, args=(clienthandler, addr)).start() 
```

### Dealing with race conditions. 

Is the threading clients process enough to keep our server under optimal performance? 

In real world servers race conditions must be handled because two clients
may try to write into the same memory allocation at the same time. Therefore, we also need to implement lock mechanisms on 
the ClientHandlers objects to avoid race conditions. The following code is an example that will help you to avoid race conditions in 
your server

```python
import threading
write_lock = threading.Lock() # creates the lock

# lock adquired only client1 can write in memory allocation
write_lock.acquire() 
# clienthandler1 writes in the memory allocation
write_lock.release() # lock is released
# other clients now can adquire the lock to write in the same memory allocation. 
```

## Your Job in this Lab

1. Implement all the methods marked as TODO in your server.py file. Note that in some methods you only need 
to copy and paste your old code from lab3. There are also some methods in the server implemented on lab3 that
are not needed anymore or must me moved to the ClientHandler class implementation

2. Implement all the methods marked as TODO in your clienthandler.py file

3. Open a command line windows and type the following command: 
   
   ```shell script
      python3 server.py
   ``` 
   
   If there are no errors, you should see the following output:
    
   ```shell script
      Listening at 127.0.0.1/12000 
   ``` 
   Note that the ip and port may be different in your case if you modified the server parameters. 
   
   Note that now you are running your own server (not the one you run in lab 2)

4. Open a command line windows (don't kill the one with the server) and type the following command: 
    
    ```shell script
      python3 client.py
    ``` 
    The above commands will run your client #1
    
    If no errors, the windows in your client should show:
    ```shell script
      {'clientid': 60644} has successfully connected to 127.0.0.1/12000
      Data acknowledged by server and you passed the test
    ``` 
    Note that the client id shown in your client windows may be different than the one shown here

5. Go to your clienthelper.py code in this lab and modify the student info in the request. 

6. Repeat step (4) using a new command line windows. This will run your second client.
   
    For the second time you run client.py (second client in a different terminal windows)
    ```shell script
      {'clientid': 60645} has successfully connected to 127.0.0.1/12000
      Data acknowledged by server and you passed the test
    ``` 
   
   Note that the client id shown in your client windows may be different than the one shown here
 
   
5. Take a look at your server windows where you run the server, you should see similar output as the one below
with your student info:

    ```shell script
       Listening at 127.0.0.1/12000
       Connected: Student: Alice Brown, Github Username: abrown, sid: 123456789
       Connected: Student: Bob Chen, Github Username: bchen, sid: 987654321
    ```

    As you can see in the above example, Alice and Bob are both connected at the same time to the server, and 
    can make asynchronous (pipelined) requests without blocking the main thread. 






