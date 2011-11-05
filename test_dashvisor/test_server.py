from nose import tools

from dashvisor.backends import backend

from test_dashvisor.cases import SupervisorTestCase



class TestServer(SupervisorTestCase):
    def setUp(self):
        self.server = backend.servers['localhost']
        self.server.start_all()

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
        tools.assert_equals(
            self.server.status,
            {}
        )
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

    def test_start(self):
        self.server.stop('a:x')
        self.server.refresh()
        self._assert_stopped('a:x')
        self.server.start('a:x')
        self._assert_stopped('a:x')
        self.server.refresh()
        self._assert_running('a:x')


