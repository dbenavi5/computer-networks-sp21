# import socket

# from Project.server.client_handler import ClientHandler


class ClientHelper:

    def __init__(self, client):
        self.Menu = None
        self.client = client
        self.student_name = 'Name: Diana Benavides'  # TODO: your name
        self.student_id = 'SID: 920652002'  # TODO: your student id
        self.github_username = 'Github username: dbenavi5'  # TODO: your github username

    def create_request(self, option):
        """
        TODO: create request with a Python dictionary to save the parameters given in this function
              the keys of the dictionary should be 'student_name', 'github_username', and
              'sid'.
        :return: the request created
        """

        request = {'payload': None, 'headers': {}}
        if option == 1:
            self.send_request(request)
        elif option == 2:
            # create menu object protocol
            menu = self.Menu.print_menu()
            self.send_request(menu)
        # elif option == 3:
        return request

    def send_request(self, request):
        """
        TODO: send the request passed as a parameter
        :request: a request representing data deserialized data.
        """
        self.client.send(request)

    def process_response(self):
        """
        TODO: process a response from the server
              Note the response must be received and deserialized before being processed.
        :response: the serialized response.
        """
        while True:
            data = self.client.receive()
            if not data:
                break
            print('Data acknowledged by server and you passed the test')

    def start(self):
        """
        TODO: create a request with your student info using the self.request(....) method
              send the request to the server, and then process the response sent from the server.
        """

        option = self.Menu()
        self.send_request(self.create_request(option))
        self.process_response()
        # self.handler(getUserServerIpAddr, getUserPort, getClientName)
        # while True:

        # request = self.create_request(self.student_name)
        #
        # self.send_request(request)
        # self.process_response()
