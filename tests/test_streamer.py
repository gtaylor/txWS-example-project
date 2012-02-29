from twisted.test  import proto_helpers
from twisted.trial import unittest

from src.protocols.websockets import EchoUpper

class EchoUpperTestCase(unittest.TestCase):
    def setUp(self):
        self.proto = EchoUpper()
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def test_dataReceived(self):
        self.proto.dataReceived('abc')
        self.assertEqual(self.tr.value(), 'ABC')
