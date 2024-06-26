#######################################################################################
# File:             menu.py
# Purpose:          CSC645 Assigment #1 TCP socket programming
# Description:      Template Menu class. You are free to modify this
#                   file to meet your own needs. Additionally, you are
#                   free to drop this Menu class, and use a version of yours instead.
# IMPORTANT:        This file can only resides on the server side.
# Usage :           menu = Menu() # creates object
#
########################################################################################

class Menu:
    """
    IMPORTANT MUST READ: The Menu class is the user interface that acts as a communication bridge between the user
    and the Client-Server architecture of this application. The Menu is always located on the Server side (machine
    running the server). However, it must be printed on the Client console by the ClientHelper object. In order to
    accomplish this, students must create a
    """

    def __init__(self, client):
        self.client = client

    @staticmethod
    def print_menu(self):
        """
        TODO: shows the following menu on the client side
        ****** TCP/UDP Network ******
        ------------------------------------
        Options Available:
        1.  Get users list
        2.  Send a message
        3.  Get my messages
        4.  Send a direct message with UDP protocol
        5.  Broadcast a message with CDMA protocol
        6.  Create a secure channel to chat with your friends using PGP protocol
        7.  Join an existing channel
        8.  Create a Bot to manage a future channel
        9.  Get the Routing Table of this client with Link State Protocol
        10. Get the Routing Table of this network with Distance Vector Protocol
        11. Turn web proxy server on (extra-credit)
        12. Disconnect from server

        Your option <enter a number>:
        """
        print('*' * 6, 'TCP/UDP Network', '*' * 6)
        print('Options Available:')
        print('1.  Get users list')
        print('2.  Send a message')
        print('3.  Get my messages')
        print('4.  Send a direct message with UDP protocol')
        print('5.  Broadcast a message with CDMA protocol')

        input('Your option <enter number>: ')

        self.option = input

    @staticmethod
    def option():
        """
        TODO: Ask the user to select an option from the menu
              Note. you must handle exceptions for options chosen that are not in the allowed range
        :return: an integer representing the option chosen by the user from the menu
        """
        option = 0
        try:
            # check menu options
            if option == 1:
                return 1
            elif option == 2:
                return 2
            elif option == 3:
                return 3
            elif option == 4:
                return 4
            else:
                return 5

        except Exception as error:
            if option is not range(5):
                print(error)

        return option

    @staticmethod
    def request_headers():
        """
        TODO: In this method students implement the headers of the menu. That's it, the options the server expect
              for each requests from the client related to this menu. For example, the headers for option 2,
              the expected headers in a client request are {'option':<integer>, 'message':<string>, 'recipient':<integer>}
        """
        headers = {'option': None, 'message': {}, 'recipient': None}

        return headers

    @staticmethod
    def response_headers():
        """
        TODO: In this method students implement the headers of the menu. That's it, the options the server sends to
              the client for each response related to this menu. For example, the headers for the response of option 3
              are {'option':<integer>, 'messages':<Python Dictionary>}
        """
        headers = ""
        return headers
