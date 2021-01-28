########################################################################################################################
# Class: CSC645-01 Computer Networks SFSU
# Lab3: TCP Server Socket
# Goal: Learning Networking in Python with TCP sockets
# Student Name:
# Student ID:
# Student Github Username:
# Program Running instructions: python3 server.py # compatible with python version 3
#
########################################################################################################################

# don't modify this imports.
import socket
import pickle
from threading import Thread


class Server(object):
    """
    The server class implements a server socket that can handle multiple client connections.
    It is really important to handle any exceptions that may occur because other clients
    are using the server too, and they may be unaware of the exceptions occurring. So, the
    server must not be stopped when a exception occurs. A proper message needs to be show in the
    server console.
    """
    MAX_NUM_CONN = 10  # keeps 10 clients in queue

    def __init__(self, host="127.0.0.1", port=12000):
        """
        Class constructor
        :param host: by default localhost. Note that '0.0.0.0' takes LAN ip address.
        :param port: by default 12000
        """
        self.host = host
        self.port = port
        self.server = None  # TODO: create the server socket
        # self.handlers = {}  # ignore this for this lab. It will be used in lab 4

    def _bind(self):
        """
        # TODO: bind host and port to this server socket
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _listen(self):
        """
        # TODO: puts the server in listening mode.
        # TODO: if successful, print the message "Server listening at ip/port"
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _accept_clients(self):
        """
        #TODO: accept clients when they connect, and creates the client handler
               after accepting the client, creating the client handler, and
               send the client id to the client, you should call the
               process_request(....) method next because after the client id
               is sent, the client will send a request with the student info.
               Recall that the server must acknowledge that it received
               the student info after processing the data
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _sendID(self, clienthandler, clientid):
        """
        TODO: sends the client id to the client
        :clienthandler: the handler created by the server for the client
        :clientid: an integer representing the client id assigned to the client
        """
        pass  # remove this line after implemented.

    def _process_request(self, clienthandler, request):
        """
        TODO: process a request from the client and sends
              a response back acknowledging that the data was received
              here is where you retrieve the student info from your client
              and print it on the server side
        :clienthandler: the handler created by the server after accepting the client
        :request: the request from the client. It must be already deserialized.
        """
        pass  # remove this line after implemented.

    def run(self):
        """
        Already implemented for you
        Run the server.
        :return: VOID
        """
        self._listen()
        self._accept_clients()


# main execution
if __name__ == '__main__':
    server = Server()
    server.run()
