from xmlrpclib import ServerProxy
from urlparse import urlparse

from django.utils.datastructures import SortedDict



class Server(object):
    def __init__(self, connection_string):
        self.name = urlparse(connection_string).hostname
        self.connection = ServerProxy(connection_string)

    def refresh(self):
        self.status = SortedDict(("%s:%s" % (i['group'], i['name']), i) for i in self.connection.supervisor.getAllProcessInfo())

    def stop(self, name):
        return self.connection.supervisor.stopProcess(name)

    def start(self, name):
        return self.connection.supervisor.startProcess(name)

    def restart(self, name):
        self.stop(name)
        self.start(name)
