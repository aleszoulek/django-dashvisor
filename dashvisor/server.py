from xmlrpclib import ServerProxy, Fault
from urlparse import urlparse

from django.utils.datastructures import SortedDict



class Server(object):
    def __init__(self, connection_string):
        self.name = urlparse(connection_string).hostname
        self.connection = ServerProxy(connection_string)

    def refresh(self):
        self.status = SortedDict(("%s:%s" % (i['group'], i['name']), i) for i in self.connection.supervisor.getAllProcessInfo())

    def stop(self, name):
        try:
            return self.connection.supervisor.stopProcess(name)
        except Fault, e:
            if e.faultString.startswith('NOT_RUNNING'):
                return False
            print e, e.faultString
            raise

    def start(self, name):
        try:
            return self.connection.supervisor.startProcess(name)
        except Fault, e:
            if e.faultString.startswith('ALREADY_STARTED'):
                return False
            print e, e.faultString
            raise

    def restart(self, name):
        self.stop(name)
        return self.start(name)
