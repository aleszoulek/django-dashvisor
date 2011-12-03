from django.conf import settings
from django.utils.datastructures import SortedDict

from dashvisor.server import Server



class Backend(object):
    def __init__(self):
        self.servers = SortedDict()
        fp = open(settings.DASHVISOR_CONFIG_FILE)
        index = 0
        for line in fp.xreadlines():
            id = str(index)
            server = Server(line.strip(), id=id)
            self.servers[id] = server
            index += 1
        fp.close()

    def refresh(self):
        for s in self.servers.values():
            s.refresh()


