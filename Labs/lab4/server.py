# don't modify this imports.
import socket
from threading import Thread
from clienthandler import ClientHandler


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
        TODO: copy and paste your implementation from lab 3 for self.server socket property
        """
        self.host = host
        self.port = port
        self.server = None  # your implementation for this socket here
        self.handlers = {}  # initializes client_handlers list

    def _bind(self):
        """
        TODO: copy and paste your implementation from lab 3
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _listen(self):
        """
        TODO: copy and paste your implementation from lab 3
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _accept_clients(self):
        """
        #TODO: Modify your implementation from lab 3, so now the
               server can support multiple clients pipelined.
               HINT: you must thread the handler(...) method
        :return: VOID
        """
        pass  # remove this line after implemented.

    def _sendID(self, clienthandler, clientid):
        """
        TODO: delete this method. It is not needed anymore on the Server class
              because the client handler object is the one that will send the
              client id to the client.
        :clienthandler: the handler created by the server for the client
        :clientid: an integer representing the client id assigned to the client
        """
        pass  # remove this line after implemented.

    def _process_request(self, clienthandler, request):
        """
        TODO: delete this method. This work will be done by the client handler object
        :clienthandler: the handler created by the server after accepting the client
        :request: the request from the client. It must be already deserialized.
        """
        pass  # remove this line after implemented.

    def _handler(self, clienthandler, addr):
        """
        TODO: create an object of the ClientHandler.
              see the clienthandler.py file to see
              the parameters that must be passed into
              the ClientHandler's constructor to create
              the object.
              Once the ClientHandler object is created,
              add it to the dictionary of client handlers initialized
              on the Server constructor (self.handlers)
        :clienthandler: the clienthandler child process that the server creates when a client is accepted
        :addr: the addr list of server parameters created by the server when a client is accepted.
        """
        pass  # remove this line after this method is implemented

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
