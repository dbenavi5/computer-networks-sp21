# TCP/UDP Centralized Client-Server Network

Please use this README file (or a new one) to provide the following documentation for this project:

* Your name and student id
* General description of the project (a few sentences)
* If you used external Python modules/libraries. Provide a requirements.txt file in this repository
* Python version and compatibility issues (if any). Your project must be run exactly as in the running instructions
  described below in this file
* Attach screenshots or videos to this file to illustrate how your program works for all the options in the menu. This
is your proof that the project was working on your side.
* A few sentences about all the challenges you found during the implementation of this project and
how you overcame them. Please be honest here.

## Note that failure to provide the above docs will result in a 30% deduction in your final grade for this project. 

## Project Description and Detailed Guidelines (must read)

Detailed guidelines about this project can be found in this file. Failure to follow them may result in a bad grade in your project. Take this into consideration. Please read them carefully, and don't hesitate to ask the instructor for clarification if needed. 

The project goal is to create a basic command line TCP/UDP Server-Client architecture network to provide basic services to multiple clients.

## Project Template. 

This project template consist in two folders (Client and Server).

   * Client Folder
       1. client.py -- copy and paste from your lab2 implementation. 
       2. clienthelper.py -- implement this file based on the functionality needed for this project

   * Server Folder
        1. server.py -- copy and paste from your lab4 implementation. 
        2. clienthandler.py -- implement this file based on the functionality needed for this project
        3. menu.py -- implement the methods marked as TODO
        
   ***IMPORTANT: if needed, you can add more files to this project as its implementation progresses. However,
   you are not allowed to modify the code from client.py and server.py once you copied and pasted it from
   the labs. The only values students are allowed to modify in server.py are the IP address and port of the server***

## Project Requirements and Output Examples (***must read***)

The following are the guidelines you must follow to implement this project.

***IMPORTANT: in this README file when I refer to server or client, I am not referring to a particular file. I am, 
however, referring to all the files on those sides. To refer to a specific file, I will mention the name of the 
file. For example, server.py***

### Server

The server.py is the entry point file to execute the server for this app.

```
python3 server.py
```

Once the server is executed (assuming no errors), then the server must log in screen the following info about its
status. We assume here that the server is run from a machine with IP address 10.0.0.49 and port 12000

```
Server is running without issues
Listening at 10.0.0.49/12000
```

Note that from this point on, the server must log all the activity in its screen. So, for example, if a clients connects
it must show a message stating that the id of the client that connected to the server. Also, if at execution time, the
server has issues or thrown exceptions, it should inform of them on screen without stopping its execution.

### The Client

***Note that server and client are two independent applications in the same network and may be executed in different machines.
If you do not have access to a second machine, you can run both in the same machine (same IP address but different ports)***

To run the client (same machine or different machine than the server)

```
python3 client.py
```
If everything goes as expected, the next step would be asking the user to enter the IP address and port of the server,
and the name of the client

Next, your program should show in screen the client's name and id assigned by the server. Similar to the following example

```
Enter the server IP Address: 127.0.0.1
Enter the server port: 12000
Enter a username: Nina
Successfully connected to server: 10.0.0.49/12000
Your client info is:
Client Name: Nina
Client ID: 50851
```

Note that the output "Successfully connected to server: 10.0.0.49/12000" must come from your client.py. The other
outputs (client name and client id) are printed out by the clienthelper.py.

### The Menu

Even though the client side of this app is the one printing the menu for the user, the menu.py file that has all the
logic for the menu is located on the server side of this application.

Why not to put the menu.py on the client folder then?

Think about it, in a real Client-Server application, the server is the one serving the contents of the application not
the other way around. For instance, in the HTTP protocol, if wants to do something in google.com, it needs to send a
request to Google server, and it will send a response with the HTML code of the site. So, then the client's browser
will render the HTML code and google.com page is served to the user. So, the first time a request like this is done,
the HTML file resides on the server side. However, the second time it is requested, it may be already cached on the client
side and served from there. That is why the menu cannot be placed on the client folder of your application.

How, then, the client can have access to the menu in my application?

That is a problem that you must solve by creating a basic protocol that allows the client to use the menu that
is located on the server side. HINT: you can also create a cache for the menu, so your protocol doesn't need to
be requesting the menu from the server everytime an user wants to interact with it.

The next step in your program is to show the menu to the user. (on the client side of course). Your program, then,
will wait for the user to enter an option from the menu.

```
****** TCP/UDP Network ******
------------------------------------
Options Available:
1.  Get users list
2.  Send a message 
3.  Get my messages 
4.  Send a direct message with UDP protocol
5.  Broadcast a message with CDMA protocol
6.  Create a secure channel to chat with your friends using PGP protocol
7.  Join an existing channel
8.  Create a Bot to manage a future channel
9.  Map the network
10. Get the Routing Table of this client with Link State Protocol
11. Get the Routing Table of this network with Distance Vector Protocol
12. Turn web proxy server on (extra-credit)
13. Disconnect from server

Your option <enter a number>:

```

### Menu options (explained)

Next, all the options from the menu are explained in detail with output examples.

#### Option 1: Get Users List
   
When users select this option the client helper sends a request to the server asking for a list of all the users connected to it.
The server sends that list, and the info from those users are shown in the client console. The info from the users connected
must be shown in the following format <username:client_id>. Note that users that were connected to the server at
some point, but are not connected at the time of the request is made, must not be in that list.

Here is an example of the output needed for option #1
  
```
Your option <enter a number>: 1

Users connected: 4
Jose:2345, Nina:8763, Alice:1234, Bob:4566
```

  
#### Option 2: Send a message

When this option is selected by the user, the client helper sends a request to the server containing the option selected,
from the menu, the message entered by the user, and the recipient id. When the client handler receives this requests,
it will need to find the client handler of the recipient of the message, and save the message there. After that,
the client handler (the one related to the sender) will send an acknowledge response to the sender to let the
sender know that the message was received.

***Note that this is not a direct message method. The messages sent are saved on the server (client handler)
until the recipient requests them in option 3***

The following is an example of the output expected when the user selects option 2.

```
Your option <enter a number>: 2
Enter your message: Hello World!
Enter recipient id: 50922
Message sent!
```

***Note that the recipient's id is the client's id of the recipient of the message.***

#### Option 3: Get my messages

In this option, a user can requests to the server all the unread messages sent from other users.

HINT: you can implement a Python list to save all the messages sent from other users in your client handler and then
when the client requests them, your client handler only has to sent a response back with all those messages.

***IMPORTANT: only unread messages are included in the response.***

The following is an example of the expected output for option 3 where the user had 2 unread messages

```
Your option <enter a number>: 3

Number of unread messages: 2
2019-08-05 17:45: Hello World! (broadcast message from Nina)
2019-08-05 17:52: This is Bob. What are you doing? (private message from Bob)
```
#### Option 4: Send a direct message with UDP protocol

In this option, the message sent by the user is not saved on the list of messages in the client handler of the
recipient. It is, however, sent directly to the recipient in real time (one way only).

***IMPORTANT: When using this option. There is no way to know if the message arrived to its destination or was lost. The
only way to confirm if the message arrived to its destination is if the recipient of the message selects this option
again and sends a direct message to the sender stating that he/she received the message***

Hint: threading is needed to implement this option. Otherwise, your receive method from your UDP socket will block 
the main thread

How to accomplish the above functionality? Use UDP protocol for one way messages only.

Here is an example of the output expected when the user selects option 4.

```
Your option <enter a number>: 4

Enter the address to bind your UDP client (e.g 127.0.0.1:6000): 127.0.0.1:6000
Enter the recipient address: 127.0.0.1:6001
Enter the message: "This is a direct message. No guaranties that the message will arrive to its destination, but it's worth
the try"

UDP client running and accepting other clients at udp address 127.0.0.1:6000
Message sent to udp address: 127.0.0.1:6001
```

#### Option 5: Broadcast a message with CDMA protocol

When option 5 is selected by the user, the message entered by the user will be broadcast to all the users that
are connected to the network. Students will also update the implementation of option 3 to make sure that data
is sent encoded by the server, and decoded on the client side using the CDMA protocol

You can implement this option using the TCP protocol, and the broadcaster must send a value to the server 
indicating the amount of responses from users the server hod before they are released to the broadcaster. The 
responses sent by the server must be encoded using the CDMA protocol, and decoded by the broadcaster with the
same protocol. 

Since you already have a TCP persistent connection established with the server, you could take advantage of this
and broadcast to all the client handlers. 

***IMPORTANT: from the receiver perspective there is no difference between a broadcast message, or a message 
 sent using option 2 because all the messages are saved on the same list of messages from each client handler.
 However, in this step you must update your implementation of option 3 to meet the requirements of option 5 to
 encode all the messages sent from the server using the CDMA protocol***

Here is an example of the output expected when the user selects option 5.

```
Your option <enter a number>: 5

Enter the message: "This is a direct broadcast message. Anyone out there?"

Message broadcast!.

```

#### Option 6: Create a secure channel to chat with your friends 

When option 6 is selected, it will create a ***SECURE*** channel for other users to join. (like in a real chat)

In order to create this channel, the user needs to input a channel id, and send the request to the server.

***Once the server receives the request, it will create public and private keys for that new channel with RSA. 
The public key of the channel will be shared among all the users that request to join the channel, and 
the private key will be shared only with the admin of the channel. Transmissions in the chat must be encrypted 
and decrypted using those public and private keys with a basic implementation of the PGP protocol***

Once the secure channel has been created, the client is put in listening mode waiting for other members to join the chat.
(option 5). Only the owner/admin of the channel can close it by entering '#exit'. Once the channel is closed, 
the client console will show the user menu again.

***IMPORTANT: (1) The implementation of the channel (not how user interact on the channel) is synchronous. That's it, 
the channel runs on the main thread of the client. In other words, the user won't see the main menu again until the
channel is closed by the admin. (2) All the users that joined to new channel must be able to chat asynchronously. That's it, a user
can send as many messages as needed, and those messages don't need to wait for other users to respond. In other words, a
message from one user cannot block the main thread. This must work like a real chat***

Here is an example of the output expected when the user selects option 6.

```
Your option <enter a number>: 6

Enter the new channel id: 23456

Private key received from server and channel 23456 was successfully created!

----------------------- Channel 23456 ------------------------

All the data in this channel is encrypted

General Admin Guidelines:
1. #nina is the admin of this channel
2. Type '#exit' to terminate the channel (only for admins)


General Chat Guidelines:
1. Type #bye to exit from this channel. (only for non-admins users)
2. Use #<username> to send a private message to that user.

Waiting for other users to join....
```

#### Option 7: Join an existing channel

A user selecting option 7 will request to the server to be joined into an existing channel.

How to implement this functionality? HINT: when you implement option 6, the client handler of the client
that creates the channel can have a list with all the users that joined this channel. So, when a user
decides to join a channel using this option, then you must find the client handler that has the channel
and add this user to that channel.

***IMPORTANT: when a new user joins a secure channel, the client will receive the public key of that channel sent 
by the server. The client of this user must implement the PGP protocol to meet the security transmission
protocols established by the server***

Below is an example of the output that represents the joining process for several users

```
Your option <enter a number>: 7

Enter channel id you'd like to join: 23456

----------------------- Channel 23456 ------------------------

All the data in this channel is encrypted

jortizco just joined
alice and #bob are already on the channel.
nina is the admin of this channel

Chat Guidelines:
Type #bye to exit from this channel. (only for non-admins)
Use #<username> to send a private message to that user.

alice> Hello jortizco
jortizco> Hello alice, who is the moderator of this chat?
nina> Hello alice, and jortizco. I am the admin. How can I help you?
alice> Something came up and I gotta go. See you later guys!.
alice> #bye
alice left the channel.
bob> It looks like alice was in a hurry.
jortizco> agree.
jortizco> #nina do you have a minute to talk in private?
nina> #jortizco of course. You are already talking to me in private when you use the '#' before my username
jose> #nina Cool!
nina> Ok guys I got to go. Bye
nina> #exit

Channel 23456 closed by admin.


****** TCP/UDP Network ******
------------------------------------
Options Available:
1.  Get users list
2.  Send a message 
3.  Get my messages 
4.  Send a direct message with UDP protocol
5.  Broadcast a message with CDMA protocol
6.  Create a secure channel to chat with your friends using PGP protocol
7.  Join an existing channel
8.  Create a Bot to manage a future channel
9.  Map the network
10. Get the Routing Table of this client with Link State Protocol
11. Get the Routing Table of this network with Distance Vector Protocol
12. Turn web proxy server on (extra-credit)
13. Disconnect from server

Your option <enter a number>:
```

***Note that everyone connected to the channel sees the same output than everyone else on their screens. The only
exception to this rule happens when a private message is sent to a user with #username, in that case, the sender
and the receiver are the only ones that can see such message on the channel***

#### Option 8: Create a Bot to manage a future channel

When this option is selected, the system creates a bot to manage a future channel. Once a client sends a request
to the server to create a bot, the server will create a token for that bot. The token must be a SHA1 hash of a
concatenation of (1) the bot name and (2) the client id. This will make the bot's token unique among all the bots
created on the same server by other users.

After the server assigns a token to our new bot, it will send a response with all the disabled permissions that can be
be enabled for the new bot. The user, then, will have to enter an integer representing the set of permissions that will
be enabled for that bot. For example, if the user enters 145, the server will enable permissions 1, 4 and 5 for that bot.
(see the example output for more details about the permissions)

If all goes as expected, the server will send to the client the new bot configuration, and the client will print it
for the user.

***Note that the bot you create in this option is for a future channel. You cannot create a bot for an existing channel because
it is not pipelined and it works on the main thread. When a channel is created, it will scan for active bots created
by the admin of the channel, and will join them automatically***

The following is an example of the output for creating a bot

```
Your option <enter a number>: 8

Enter the name of your bot: MelindaBot

The disabled permissions for this bot are:
1. Welcome users right after they join a channel.
2. Show a warning to the users when they send words that are not allowed
3. Drop users from the channel after 3 warnings
4. Compute the response time of a message when the user request it
5. Inform the user when it has been inactive on the channel for more than 5 minutes.

Enter an integer to enable a set of permissions: 145

MelindaBot's Configuration:
Token: cf23df2207d99a74fbe169e3eba035e633b65d94
Permissions Enabled: 145
Status: ready
```

After a bot is setup and active, if we select option 7 to create a new channel, the channel will send a request
to the server to check if there are bots enabled owned by the admin of the channel, if so, then it will automatically join
them to the new channels and the bots will be able to perform the actions defined by their enabled permissions.

The following is a basic example of our new bot in a new channel:

```
----------------------- Channel 23456 ------------------------

All the data in this channel is encrypted

#melindaBot joined.
#jortizco joined
#alice and #bob are already on the channel.
#nina is the admin of this channel

Chat Guidelines:
1. Type #bye to exit from this channel. (only for non-admins users)
2. Use #<username> to send a private message to that user.

melindaBot> Welcome #jortizco.
jortizco> I am wondering what's the response time of this message
melindaBot> jortizco, the response time of your message is 0.01 milliseconds
melindaBot>> #alice you have been very quiet for the last five minutes. We miss you!

```
#### Option 9: Get the Routing Table of this client with Link State Protocol

In this option the server will map the network upon client request. Mapping the network in this assignment means getting 
a table with all the distances between nodes/machines. If one or more clients are running in the same machine, then the server must 
assign random distances to those clients.

The following is an example of the output needed for this option:

```
Your option <enter a number>: 9

Routing table requested! Waiting for response.... 

Network Map: 

         |  Nina   |  Alice  |   Jortizco   |    Bob      |
-----------------------------------------------------------
Nina     |   0     |    15   |     10       |     -       |
Alice    |   15    |    0    |     30       |     11      |
Jortizco |   10    |    30   |     0        |     25      |
Bob      |   -     |    11   |     25       |     0       |
```
 
#### Option 10: Get the Routing Table of this client with Link State Protocol

In this option the client will request its routing table to the server using itself as the source node. Then the 
client will print the routing table for the user.  

A map of the network must be printed (implementation of option 9) and next the routing table. This way, it is easy
to check if the server did mistakes with the computations of the shortest distances. 

The following is an example of the output needed for this option:

```
Your option <enter a number>: 10

Routing table requested! Waiting for response.... 

Network Map: 

         |  Nina   |  Alice  |   Jortizco   |    Bob      |
-----------------------------------------------------------
Nina     |   0     |    15   |     10       |     -       |
Alice    |   15    |    0    |     30       |     11      |
Jortizco |   10    |    30   |     0        |     25      |
Bob      |   -     |    11   |     25       |     0       |

Routing table for Nina (id: 50851) computed with Link State Protocol: 

|  destination |              Path                 |      Cost      | 
-------------- | --------------------------------  | -------------  |
|    Alice     |          {Nina, Alice}            |       15       |
|   Jortizco   |        {Nina, Jortizco}           |       10       |
|     Bob      |      {Nina, Jortizco, Bob}        |       35       |
```

#### Option 11: Get the Routing Table of this network with Distance Vector Protocol

The implementation of this option is similar to the one from option 10. However, in this case and after computing/updating
the map of the network, the server will compute the routing table for this client using the Distance Vector Protocol.
In addition, the server will also include in the response the time taken to compute the routing table. 

***IMPORTANT: the routing table received from the server is the same routing table for all the clients because the
Distance Vector protocol determines the shortest path from all the pair of nodes in the network***

The following is an example of the output needed for this option. We assume here that Bob disconnected from the 
network:

```
Your option <enter a number>: 11

Routing table requested! Waiting for response.... 

Network Map: 

         |  Nina   |  Alice  |   Jortizco   |
---------------------------------------------
Nina     |   0     |    2    |      7       |    
Alice    |   2     |    0    |      1       |     
Jortizco |   7     |    1    |      0       |     


Routing table computed with Distance Vector Protocol: 

         |  Nina   |  Alice  |   Jortizco   |
---------------------------------------------
Nina     |   0     |    2    |      3       |    
Alice    |   2     |    0    |      1       |     
Jortizco |   3     |    1    |      0       |     
```

As you can see in the routing table, some of the distances were updated to reflect the shortest path 
between nodes. 

#### Option 12: Turn web proxy server on (Note that this option is extra-credit and optional 5%)

This section is extra-credit and optional, if you are implementing this section, then read "Web Proxy Server" section below.
Otherwise, when the user selects this section, just print "coming soon" in console. 

***Students implementing this option as expected will be awarded with 5% extra-credit that will be added to the 
final grade of the course. However, students can only do the extra-credit if they finished all the mandatory
options (1 to 10) in this assignment***

***IMPORTANT: I give partial credit (1%) for each option implemented in the extra-credit***

This extra-credit is explained in detail after the guidelines of option 13 below. 

#### Option 13: Disconnect from server

A user selecting this option will requests to be disconnected from the server. The client sends the request to the server, then the server performs a cleanup of all the data related to that client in the server, and finally close the connection with that client socket. In addition, you also have the option to disconnect the client on the client side. Although this may work just fine, it is more prone to errors since the server still needs to do the cleanup of data for that socket (which do not exist anymore). 

# Web Proxy Server (option #12 in main menu)

Note that this extra-credit section is an addition to the TCP Client-Server project. This part of the assignment is optional. 

```
****** TCP/UDP Network ******
------------------------------------
Options Available:
1.  Get users list
2.  Send a message 
3.  Get my messages 
4.  Send a direct message with UDP protocol
5.  Broadcast a message with CDMA protocol
6.  Create a secure channel to chat with your friends using PGP protocol
7.  Join an existing channel
8.  Create a Bot to manage a future channel
9.  Map the network
10. Get the Routing Table of this client with Link State Protocol
11. Get the Routing Table of this network with Distance Vector Protocol
12. Turn web proxy server on (extra-credit)
13. Disconnect from server

Your option <enter a number>: 12
```

When in the main menu the user selects option 12 from the main menu, then the following menu appears on screen

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```

### Option 1: Turn web caching On. 
  
Once this option is selected, the user should be informed that the web caching option is on. Note how the next time the 
menu is loaded when this option is active, the option has changed to "turn web caching Off". 
  
```
Your option <enter a number>: 1
Web caching is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```
Once the web caching system is active in the proxy server, all the GET requests done in option 4, 
need to be cached. Every time we send a request to a original server (i.e google), the proxy should check, 
first, if that resource already exists in the cache folder. Otherwise, the resource needs to be cached. 
The files cached contain the response from the original server (headers and body). 
The name of the files should be a hashed identifier with extension .pickle. 
The following are examples of files cached by the proxy server. 

```
53d9b3a0-4c87-11ea-9d7f-784f4387efce.pickle
d54442c6-4c86-11ea-9d7f-784f4387efce.pickle
```
You should keep track in memory of the identifier of each file, last_modified_date, and the domain (server site). 
The next time the proxy server requests a resource that already exists in the cache. It should hand to the user only 
the version cached. 

### Option 2: Turn authentication On.

Similar to option 1, when option 2 is turned on, the next time the proxy server menu is loaded, it should look like the following menu:

```
Your option <enter a number>: 2
Web authentication is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication Off
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```

***Note how option 2 now says "Turn authentication Off"***

When on, this option should implement authentication services. There are sites that ask you to provide your credentials 
(if already registered in the site) in order to access some of their resources or to simply login into the site. 
After making a request, this option should ask first for username and password. See option 4  to see 
examples about authentications using requests.

### Option 3: Turn private browsing Off.

By default, this option needs to be turned On automatically when the proxy server is activated for the first time. 
This option allows multiple clients to mask their IP addresses. 
For instance, let's assume that a client has IP address 180.4.4.23, and the proxy server running in a different machine 
has IP address 167.7.9.87. If private browsing is active, and the client makes a request to www.google.com then, 
from the eyes of google, the request is coming from IP address 167.7.9.87. However, the request is really 
coming from 180.4.4.23. Thus, the proxy server is hiding the client IP address from the original server. This is useful 
when browsing in private mode is required, or the client's IP address has been blocked to access certain resources in a site. 

### Option 4: Send a request (GET, HEAD OR POST): 

This option allows a client to create GET, HEAD and POST requests. 

* GET requests 

GET requests are done by a client in order to get complete responses from original servers that are filtered by a proxy server. Additional data requested is appended to the URL part of the header. For instance, a request to www.example.com attaching name="Jose" and lastname="Ortiz" will be send in the request header as www.example.com?name=Jose&lastname=Ortiz 

* HEAD requests

HEAD requests are different from GET requests. When a HEAD request is performed, the original server will send only the headers of the response (not the actual data such as the HTML of a file). This is useful when you need to check if the last-modified-date header of your resource cached is outdated, and the original server has a newer version of the file you have in cache from that server. 

* POST requests

POST requests are done to add 'some sense' of security to the data sent in the request. Normally, POST requests are done when you need to submit forms or any other resource that needs to be transmitted to the server in the body of the requests. 

### Examples for option 4. 

Note that in some of the following examples, private web browsing has been turned on automatically, 
so the source IP you see in most of them is not the client IP address (127.0.0.1), 
it is the proxy IP address running in a different machine. 

GET request with authentication 'off', and trying to create a request to a resource that needs authorization.

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://api.github.com/user
Source IP address: 180.8.8.21
401 Unauthorized. Activate authentication in your proxy server and try again.
```

GET request with authentication 'on'.

```
Your option <enter a number>: 2
Web authentication is on

*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication Off
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://api.github.com/user
Source IP address: 180.8.8.21
Username: joseortizcostadev@gmail.com
Password: **********
Success 200 OK
{"login":"joseortizcostadev","id":11967132,"node_id":"....","avatar_url":"https://avatars0.githubusercontent.com/u/11967132?....}
```

GET request with authentication turned 'off', and web cache turned 'on'. Since this is the first time we access to the resource, the resource will be cached in the cache, but will be shown in screen. 

```
Your option <enter a number>: 1
Web caching is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://example.com
Source IP address: 180.8.8.21
Success 200 OK
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

```

GET request to the same resource as the one above. However, since the resource this time is cached, it will show (cached) status. In addition, we turned 'off' private browsing, and now, it shows the real source IP address. (the one from the client)

```
Your option <enter a number>: 3
Private browsing is off

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing On
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 4
request> GET https://example.com
Source IP address: 127.0.0.1
Success 200 OK (cache)
```

HEAD request example. Note that web caching only works for GET and POST requests.

```
Your option <enter a number>: 4                       
request> HEAD https://example.com
Source IP address: 127.0.0.1
Success! 200 OK
{'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Age': '558039', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Wed, 19 Feb 2020 23:07:05 GMT', 'Etag': '"3147526947+gzip"', 'Expires': 'Wed, 26 Feb 2020 23:07:05 GMT', 'Last-Modified': 'Thu, 17 Oct 2019 07:18:26 GMT', 'Server': 'ECS (sjc/4E5D)', 'X-Cache': 'HIT', 'Content-Length': '648'}

```

POST request example with name and lastname. If you inspect the response, you cab see the name and last name embedded into the form key in the response body.   

```
Your option <enter a number>: 4
request> POST http://httpbin.org/post
Source IP address: 127.0.0.1
POST keys separated by comma: name,lastname
POST values separated by a comma: Jose,Ortiz
Success 200 OK
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "lastname": "Ortiz", 
    "name": "Jose"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "24", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.22.0", 
    "X-Amzn-Trace-Id": "Root=1-5e4dc024-6acb6e343143004027059d22"
  }, 
  "json": null, 
  "origin": "73.92.230.115", 
  "url": "http://httpbin.org/post"
}

```

Failing requests need to be taken also in consideration. For example, a HEAD requests to google will fail with code status 301 (Moved permanently)

```
Your option <enter a number>: 4
request> HEAD https://google.com
Source IP address: 127.0.0.1
Note: authentication does not work with HEAD request
Request failed with status code 301
```

However, a basic GET request to google will work

```
Your option <enter a number>: 4
request> GET https://google.com
Source IP address: 127.0.0.1
Success 200 OK
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){window.google={kEI:'b8FNXr2FGMHk-gS4xZjQCg',kEXPI:'0,1353746,5663,731,223,5105,206,2954,250,10,1051,175,364,925,510,4,60,690,52,75,383,876,504,225,7,15,60,219,415288,712177,680,1197113,231,125,44,329074,1294,12383,4855,32691,15248,867,6056,22628,369,8819,8384,4859,1361,4325,4965,3024,4744,3118,7910,1,1812,1976,2044,5766,1,3142,5297,2974,873,38,1179,2975,2785,3645,1142,6290,3254,620,2883,21,318,234,1746,1192,1344,2780,517,401,2276,8,570,2226,814,779,1279,390,652,1170,202,37,291,149,1103,840,517,1466,8,49,819,3438,109,151,52,1135,1,3,2669,1839,184,1920,377,686,1261,244,503,283,1,145,44,1009,93,328,1284,16,84,417,2426,1425,821,474,1339,29,719,1039,15,3212,2845,7,438,379,503,951,3328,780,1184,70,6513,1831,832,169,899,2023,2458,1226,1462,280,420,3235,1274,108,1246,1680,481,908,2,433,1040,322,1760,2397,1953,3111,355,225,402,594,830,1,839,185,2,293,548,877,98,258,723,186,814,58,125,278,110,40,165,89,1,1668,218,242,128,1660,1,707,148,543,1237,418,414,415,474,98,3,91,299,12,1,740,41,329,1,743,18,2,52,59,28,130,1,21,49,72,14,467,127,18,98,134,62,678,353,166,42,1075,274,898,143,1136,297,66,417,443,5845084,1872,1804021,4194968,2801054,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,879,9,305,239,402,5,96,3,1,3364996,17378642,3220020,23',kBL:'lyiv'};google.sn='webhp';google.kHL='en';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);
var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script nonce="ffHmu/8Tzx0uNQvmezayDg=="></script></head><body bgcolor="#fff"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="https://www.google.com/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="https://maps.google.com/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="https://www.youtube.com/?gl=US&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.com/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.com/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I'm Feeling Lucky" name="btnI" type="submit"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}
else top.location='/doodles/';};})();</script><input value="AINFCbYAAAAAXk3Pf_KSUy6JTEhsacDOHEoQmaACNS-5" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising Programs</a><a href="/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="ffHmu/8Tzx0uNQvmezayDg==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u='/xjs/_/js/k\x3dxjs.hp.en_US.wv6Biy5pB4Y.O/m\x3dsb_he,d/am\x3dgAEBNgI/d\x3d1/rs\x3dACT90oGn6BLi3_K49plSlp17NnHesX7UkQ';
setTimeout(function(){var b=document;var a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.hp.en_US.wv6Biy5pB4Y.O/m\x3dsb_he,d/am\x3dgAEBNgI/d\x3d1/rs\x3dACT90oGn6BLi3_K49plSlp17NnHesX7UkQ';})();function _DumpException(e){throw e;}
function _F_installCss(c){}
(function(){google.spjs=false;google.snet=true;google.em=[];google.emw=false;google.pdt=0;})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22en\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22Clear Search\x22,\x22dym\x22:\x22Did you mean:\x22,\x22lcky\x22:\x22I\\u0026#39;m Feeling Lucky\x22,\x22lml\x22:\x22Learn more\x22,\x22oskt\x22:\x22Input tools\x22,\x22psrc\x22:\x22This search was removed from your \\u003Ca href\x3d\\\x22/history\\\x22\\u003EWeb History\\u003C/a\\u003E\x22,\x22psrl\x22:\x22Remove\x22,\x22sbit\x22:\x22Search by image\x22,\x22srch\x22:\x22Google Search\x22},\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x22jdx57DidmDsKEbU17xIzr-SJe_U\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();</script>        </body></html>

```

### Option 5: Turn web proxy server off

When this option is selected the proxy server is turned 'off', and the main menu is printed again. 

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing On
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off


Your option <enter a number>: 5
Web proxy server is now off

****** TCP/UDP Network ******
------------------------------------
Options Available:
1.  Get users list
2.  Send a message 
3.  Get my messages 
4.  Send a direct message with UDP protocol
5.  Broadcast a message with CDMA protocol
6.  Create a secure channel to chat with your friends using PGP protocol
7.  Join an existing channel
8.  Create a Bot to manage a future channel
9.  Map the network
10. Get the Routing Table of this client with Link State Protocol
11. Get the Routing Table of this network with Distance Vector Protocol
12. Turn web proxy server on (extra-credit)
13. Disconnect from server

Your option <enter a number>:

```

# Running the project, 

You must follow exactly these instructions in order to run and test your project. If I cannot run your project, 
as the following guidelines state, you'll get a zero in this project. No exceptions here!. So, test it properly before final submission. 

To run the server:

``` 
python3 server.py 
```
***IMPORTANT: the server can run in localhost or it can run using the IP address was assigned by your LAN to the machine 
running the server. If you set the IP address of the server to '0.0.0.0' the server socket will bind the LAN IP address assigned to 
that machine to the program and the port provided by the programmer in the server.py code***

To run a client, you have two options:

1. Run clients in different machines (LAN)
2. Run clients in the same machine as your server (localhost or LAN)

``` 
python3 client.py 
```

# Grading Rubric: 

1. This project is worth 40% of your final grade, and will be graded using a point scale where the 
maximum possible grade is 100 points. For example, a grade of 80/100 in this project will be converted to 
0.80 * 25% = 32% of 40%

3. If your server and client files run without errors or crashes, the first client is not blocking the main thread, it 
prints the menu, and you provided all the docs requested at the beginning of this README page. then +50 points. 

4. If any of the requirements from step 3 is missing, I will apply a grade (at my discretion) depending on how much 
work the student has done in the project. However, this grade will be way below the 50 points threshold. 
Please make sure to test your project properly before submission to avoid this situation. 

5. For each option of the menu that is implemented (after step 3 is successfully executed), then +5 points

6. The proxy server option (extra-credit) is 5% that will be added to your final grade at the end of the semester. This
extra-credit has also partial credit (1%) for each option completed in the proxy server.

***IMPORTANT: students can only do the proxy server extra-credit if they implemented (and completed) all the 
other options from the main menu.***

7. Late submissions will be penalized with 20 points in the final grade of this project. There won't be extensions granted
for this project because it must be finished (and submitted for grading) one week before the final exam. 




# Project Submission

Once this project is completed, set this project in the table of assignments (located in the main README file of this repository) 
to completed or done. Take into consideration that if your project is not set to completed in that table, I will assume
that the project was not submitted. 

Good luck!!!











