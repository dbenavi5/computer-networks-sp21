import threading
import pickle
import time

class ClientHandler:

    def __init__(self, server_instance, clienthandler, addr):
        self.server_ip = addr[0]
        self.client_id = addr[1]
        self.server = server_instance
        self.handler = clienthandler
        self.print_lock = threading.Lock()  # creates the print lock
        self.messages = {}
        self.sendID(self.client_id)

    # TODO: implement the ClientHandler for this project.
    def process_requests(self):
        """
        TODO: Create a loop that keeps waiting for client requests.
              Note that the process_request(...) method is executed inside the loop
              Recall that you must break the loop when the request received is empty.
        :return: VOID
        """
        while True:
            request = self.receive()
            if not request:
                break
            self.process_request(request)


    def process_request(self, request):
        """
        TODO: This implementation is similar to the one you did in the method process_request(...)
              that was implemented in the server of lab 3.
              Note that in this case, the clienthandler is not passed as a parameter in the function
              because you have a private instance of it in the constructor that can be invoked from this method.
        :request: the request received from the client. Note that this must be already deserialized
        :return: VOID
        """
        # get options
        option = request['headers']['option']
        response = {'payload': None, 'headers': {}, 'ack': -1}
        if option == 1:
            response['payloads'] = self.user_connected()
        elif option == 2:
            message = request['payloads']
            user = request['headers']['user']
            response['ack'] = self.save_message(message, user)
        elif option == 3:
            response['payload'] = self.messages
        elif option == 4:
            response['headers'] = self.direct_message()
        elif option == 5:
            response['payloads'] = self.broadcast()

        self.send(response)

    # Option 1
    def user_connected(self):

        return 0

    # Option 2
    def save_message(self, message, user):
        try:
            # search for the correct user handler that belongs to the user
            user_handler = self.server.handlers[user]
            # list messages
            message_list = user_handler.messages
            # check if the sender exits the user message list
            if self.client_id not in message_list.keys():
                message_list[self.client_id] = []
                message_info = (message, time.time())
                message_list[self.client_id].append(message_info)
                return 1
        except Exception as err:
            self.log(err[1])
        return 0

    # Option 3
    def get_message(self):
        return 0

    # Option 4
    def direct_message(self):
        return 0

    # option 5
    def broadcast(self):
        return 0

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
        data = self.handler.recv(max_mem_alloc)
        deserialized_data = pickle.loads(data)
        return deserialized_data

    def sendID(self, clientid):
        """
        TODO: send the client id to the client
        """
        clientid = {'clientid': clientid}
        self.handler.send(clientid)

    def log(self, message):
        """
        TODO: log a message on the server windows.
              note that before calling the print statement you must acquire a print lock
              the print lock must be released after the print statement.
        """
        self.print_lock.acquire()
        print(message)
        self.print_lock.release()

    def run(self):
        """
        Already implemented for you
        """
        self.process_requests()

