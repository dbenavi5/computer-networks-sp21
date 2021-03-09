########################################################################################################################
# Class: Computer Networks
# Date: 02/03/2020
# Lab3: Server support for multiple clients
# Goal: Learning Networking in Python with TCP sockets
# Student Name: Diana Benavides
# Student ID: 920652002
# Student Github Username: dbenavi5
# Lab Instructions: No partial credit will be given. Labs must be completed in class, and must be committed to your
#               personal repository by 9:45 pm.
# Running instructions: This program needs the server to run. The server creates an object of this class.
#
########################################################################################################################

import threading
import pickle


class ClientHandler:
    """
    The client handler class receives and process client requests
    and sends responses back to the client linked to this handler.
    """

    def __init__(self, server_instance, clienthandler, addr):
        """
        Class constructor already implemented for you.
        :param server_instance: passed as 'self' when the object of this class is created in the server object
        :param clientsocket: the accepted client on server side. this handler, by itself, can send and receive data
                             from/to the client that is linked to.
        :param addr: addr[0] = server ip address, addr[1] = client id assigned buy the server
        """
        self.server_ip = addr[0]
        self.client_id = addr[1]
        self.server = server_instance
        self.handler = clienthandler
        self.print_lock = threading.Lock()  # creates the print lock
        self.sendID(self.client_id)

    def process_requests(self):
        """
        TODO: Create a loop that keeps waiting for client requests.
              Note that the process_request(...) method is executed inside the loop
              Recall that you must break the loop when the request received is empty.
        :return: VOID
        """
        pass  # remove this line after this method is implemented.

    def process_request(self, request):
        """
        TODO: This implementation is similar to the one you did in the method process_request(...)
              that was implemented in the server of lab 3.
              Note that in this case, the clienthandler is not passed as a parameter in the function
              because you have a private instance of it in the constructor that can be invoked from this method.
        :request: the request received from the client. Note that this must be already deserialized
        :return: VOID
        """
        while True:
            raw_data = request.recv(1024)  # receives data from this client
            if not raw_data:
                break
            data = pickle.loads(raw_data)  # deserializes the data from the client
            student_name = data['student_name']
            github_username = data['github_username']
            sid = data['sid']
            log = "Connected: Student: " + student_name + ", Github Username: " + github_username + ", sid: " + str(sid)
            print(log)
            serialized_data = pickle.dumps(1)  # creates a stream of bytes
            request.send(serialized_data)

    def send(self, data):
        """
        TODO: serializes data with pickle, and then send the serialized data
        """
        serialized_data = pickle.dumps(data)
        self.handler.send(serialized_data)

    def receive(self, max_mem_alloc=4096):
        """
        TODO: receive the data, deserializes the data received
        :max_mem_alloc: an integer representing the maximum allocation (in bytes) in memory allowed
                        for the data that is about to be received. By default is set to 4096 bytes
        :return: the deserialized data
        """
        serialized_data = self.handler.receive(max_mem_alloc)
        deserialized_data = pickle.loads(serialized_data)
        return deserialized_data

    def sendID(self, clientid):
        """
        TODO: send the client id to the client
        """
        clientid = {'clientid': clientid}
        serialized_data = pickle.dumps(clientid)
        self.handler.send(serialized_data)

    def log(self, message):
        """
        TODO: log a message on the server windows.
              note that before calling the print statement you must acquire a print lock
              the print lock must be released after the print statement.
        """

    def run(self):
        """
        Already implemented for you
        """
        self.process_requests()
