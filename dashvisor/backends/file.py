from django.conf import settings

from dashvisor.server import Server



class Backend(object):
    def __init__(self):
        self.servers = []
        fp = open(settings.DASHVISOR_CONFIG_FILE)
        for line in fp.xreadlines():
            self.servers.append(Server(line.strip()))
        fp.close()


