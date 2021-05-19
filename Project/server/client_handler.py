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

        # Get the options
        option = request['headers']['option']
        response = {'payload': None, 'headers': {}, 'ack': -1}  # protocol
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
        users = {}
        clienthandler = self.server.handlers
        for user_id, handler in clienthandler.items():
            user = (handler.name, handler.id)
            users[user_id] = user

        return users

    def process_option(self, option):
        if option == 1:
            user_list = self.user_connected()
            self.handler.send(user_list)  # this is sent to the client so the client prints it on screen

    # Option 2
    def save_message(self, message, recipient_id):
        try:
            # 1. search for the correct user handler that belongs to the user
            recipient_handler = self.server.handlers[recipient_id]
            # 2. list messages = {} (messages from constructor)
            message_list = recipient_handler.messages
            # 3. check if the sender exits the user message list
            if self.client_id not in message_list.keys():
                message_list[self.client_id] = []
                message_info = (message, time.time())
                message_list[self.client_id].append(message_info)
                return 1
        except Exception as error:
            self.log(error[1])
        return 0

    # Option 4
    def direct_message(self):
        # send message to recipient, create protocols and match UDP port to TCP port
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
