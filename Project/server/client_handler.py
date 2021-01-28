class ClientHandler:

    def __init__(self, server_instance, clienthandler, addr):
        self.server_ip = addr[0]
        self.client_id = addr[1]
        self.server = server_instance
        self.handler = clienthandler

    # TODO: implement the ClientHandler for this project.
