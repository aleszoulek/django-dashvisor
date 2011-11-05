import time
import subprocess
from os.path import dirname, join

from unittest import TestCase


_supervisor_processes = []

class SupervisorTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        if not _supervisor_processes:
            _supervisor_processes.append(
                subprocess.Popen(['supervisord', '-n', '--configuration', join(dirname(__file__), 'supervisord_1.conf')])
            )
            _supervisor_processes.append(
                subprocess.Popen(['supervisord', '-n', '--configuration', join(dirname(__file__), 'supervisord_2.conf')])
            )
            time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        for process in _supervisor_processes:
            process.kill()
        for process in _supervisor_processes:
            process.wait()


