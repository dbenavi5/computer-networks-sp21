"""
This Python file can be used only for CSC645 projects or labs.
Students taking this class are allowed to copy and/or modify
the content of this file to meet their needs for the project.
"""
import socket


class Tracker:

    def __init__(self, port):
        """
        Class constructor
        :param port: the port that will be bind to this UDP tracker
        """
        self.port = port
        self.udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # note that '' is taking your LAN ip address by default. '0.0.0.0' will do the same
        self.udpSocket.bind(('', port))
        print("Tracker started at port {}".format(self.port))

    def send(self, message, address):
        """

        :param message: the parameter must be passed in bytes string. For example, b'this is a message'
        :param address: the address of the recipient of the message. Address in this case is a tuple (ip, port)
        :return: VOID
        """
        self.udpSocket.sendto(message, address)

    def receive(self):
        """
        :return: you are free to return the message here. As it, this is a VOID method.
        """
        while True:
            data, addr = self.udpSocket.recvfrom(1024)
            print(f'Message: {data} received from {addr}')

    def listen(self):
        """
        This method is optional. However, it put in context the action performed by the tracker when it is listening
        :return: VOID
        """
        self.receive()

    def broadcast(self, message, toSelf=False):
        """

        :param message: the message to be broadcast
        :param toSelf: True if the sender wants to broadcast the message to self. Otherwise, false
        :return: VOID
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(message, ('<broadcast>', self.port))
        print("message sent!")
        if toSelf:  # broadcast to itself
            self.listen()


if __name__ == "__main__":
    tracker = Tracker(5002)
    # tracker.listen() # to listen for messages
    tracker.broadcast(b"this is a message that is about to be broadcast", toSelf=True)

### Sample output when I run the tracker in two different machines listening to port 5002

# Tracker started at port 5002
# message sent!
# Message: b'this is a message that is about to be broadcast' received from ('10.0.0.145', 55185)
# Message: b'this is a message that is about to be broadcast' received from ('10.0.0.175', 55185)