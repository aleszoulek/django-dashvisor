from nose import tools

from dashvisor.backends import backend

from test_dashvisor.cases import SupervisorTestCase



class TestServer(SupervisorTestCase):
    def setUp(self):
        self.server = backend.servers['localhost']

    def test_refresh(self):
        tools.assert_equals(
            self.server.status,
            {}
        )
        self.server.refresh()
        tools.assert_equals(
            self.servers.status.keys(),
            []
        )


