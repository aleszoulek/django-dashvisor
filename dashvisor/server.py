from xmlrpclib import ServerProxy
from urlparse import urlparse



class Server(object):
    def __init__(self, connection_string):
        self.name = urlparse(connection_string).hostname
        self.connection = ServerProxy(connection_string)
        self.refresh()

    def refresh(self):
        self.status = self.connection.supervisor.getAllProcessInfo()
