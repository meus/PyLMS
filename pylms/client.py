__author__ = 'ben'

import telnetlib
import urllib
import pylms
from pylms.server import Server
from pylms.player import Player

class Client(Server):

    def start(self):
        self.connect()
        self.request("listen")

        while True:
            received = self.telnet.read_until("\n".encode(self.charset))[:-1]
            if received:
                status = self.request_with_results(command_string=None, received=received)

    def stop(self):
        exit()

if __name__ == "__main__":

    my_client = Client("192.168.0.24", 9090)
    my_client.start()