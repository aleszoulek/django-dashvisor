from nose import tools

from dashvisor.backends import backend

from test_dashvisor.cases import SupervisorTestCase



class TestServer(SupervisorTestCase):
    def setUp(self):
        self.server = backend.servers['0'] # localhost is first
        self.server.start_all()
        self.server.refresh()
        #import time
        #time.sleep(2)

    def _assert_stopped(self, name):
        self._assert_state(name, 0)

    def _assert_running(self, name):
        self._assert_state(name, 20)

    def _assert_state(self, name, state):
        tools.assert_equals(
            self.server.status['a:x']['state'],
            state
        )

    def test_refresh(self):
        self.server.refresh()
        tools.assert_equals(
            self.server.status.keys(),
            ['a:x', 'a:y', 'b:y', 'b:z', 'tail-everything:tail-everything']
        )

    def test_stop(self):
        self._assert_running('a:x')
        self.server.stop('a:x')
        self._assert_running('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')

    def test_stop_twice(self):
        self._assert_running('a:x')
        self.server.stop('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')
        self.server.stop('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')

    def test_start(self):
        self.server.stop('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')
        self.server.start('a:x')
        self._assert_stopped('a:x')
        self.server.refresh()
        self._assert_running('a:x')

    def test_start_twice(self):
        self._assert_running('a:x')
        self.server.start('a:x')
        self.server.refresh()
        self._assert_running('a:x')

    def test_start_all(self):
        self.server.stop('a:x')
        self.server.stop('a:y')
        self.server.refresh()
        self._assert_stopped('a:x')
        self._assert_stopped('a:y')
        self.server.start_all()
        self.server.refresh()
        self._assert_running('a:x')
        self._assert_running('a:y')

    def test_restart_running(self):
        self.server.restart('a:x')
        self.server.refresh()
        self._assert_running('a:x')

    def test_restart_stopped(self):
        self.server.stop('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')
        self.server.restart('a:x')
        self.server.refresh()
        self._assert_running('a:x')


