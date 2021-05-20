########################################################################################################################
# Class: Computer Networks
# Date: 05/19/2021
# Lab3: TCP Client Socket
# Goal: Learning Networking in Python with TCP sockets
# Student Name: Diana Benavides
# Student ID: 920652002
# Student Github Username: dbenavi5
# Instructions: Read each problem carefully, and implement them correctly.
########################################################################################################################

# don't modify this imports.
import socket
import pickle

from client_helper import ClientHelper

######################################## Client Socket ###############################################################3
"""
Client class that provides functionality to create a client socket is provided. Implement all the methods but bind(..)
"""


class Client(object):

    def __init__(self):
        """
        Class constructor
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = 0

    def connect(self, server_ip_address, server_port):
        """
        TODO: Create a connection from client to server
              Note that this method must handle any exceptions
        :server_ip_address: the know ip address of the server
        :server_port: the port of the server
        """

        try:
            self.client.connect((server_ip_address, server_port))
            self.id = self.receive()
            print(f'{self.id} connected to {server_ip_address}/{server_port}')
        except socket.error as msg:
            print(msg)

    def bind(self, client_ip='', client_port=12000):
        """
        DO NOT IMPLEMENT, ALREADY IMPLEMENTED
        This method is optional and only needed when the order or range of the ports bind is important
        if not called, the system will automatically bind this client to a random port.
        :client_ip: the client ip to bind, if left to '' then the client will bind to the local ip address of the machine
        :client_port: the client port to bind.
        """
        self.client.bind((client_ip, client_port))

    def send(self, data):
        """
        TODO: Serializes and then sends data to server
        :param data: the raw data to serialize (note that data can be in any format.... string, int, object....)
        :return: VOID
        """
        self.client.send(pickle.dumps(data))

    def receive(self, max_alloc_buffer=4090):
        """
        TODO: Deserializes the data received by the server
        :param max_alloc_buffer: Max allowed allocated memory for this data
        :return: the deserialized data.
        """
        data = self.client.recv(max_alloc_buffer)
        deserialized_data = pickle.loads(data)
        return deserialized_data

    def client_helper(self, menu, tracker):
        """
        TODO: create an object of the client helper and start it.
        """
        obj = ClientHelper(self, menu, tracker)
        obj.start()

    def close(self):
        """
        TODO: close this client
        :return: VOID
        """
        self.client.close()


# main code to run client
if __name__ == '__main__':
    server_ip = '10.0.0.49'
    server_port = 12000
    client = Client()
    client.connect(server_ip, server_port)  # creates a connection with the server
    client.client_helper()
