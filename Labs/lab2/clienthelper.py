class ClientHelper:

    def __init__(self, client):
        self.client = client
        student_name = 'Name: Diana Benavides'  # TODO: your name
        student_id = 'SID: 920652002'  # TODO: your student id
        github_username = 'Github username: dbenavi5'  # TODO: your github username

    def create_request(self, name, id, github_username):
        """
        TODO: create request with a Python dictionary to save the parameters given in this function
              the keys of the dictionary should be 'student_name', 'github_username', and
              'sid'.
        :return: the request created
        """
        student_name = self.name
        github_username = self. github_username
        sid = self.id

        request = {student_name, github_username, sid}

        return request

    def send_request(self, request):
        """
        TODO: send the request passed as a parameter
        :request: a request representing data deserialized data.
        """
        self.client.send_request(request)

    def process_response(self):
        """
        TODO: process a response from the server
              Note the response must be received and deserialized before being processed.
        :response: the serialized response.
        """
        self.client.process_response()

    def start(self):
        """
        TODO: create a request with your student info using the self.request(....) method
              send the request to the server, and then process the response sent from the server.
        """
        self.create_request()