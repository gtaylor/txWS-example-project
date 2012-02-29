from twisted.internet.protocol import Factory, Protocol
from twisted.python import log

class WebSocketServerFactory(Factory):
    """
    This is used by twisted.internet.TCPServer to create TCP Servers for each
    port the server listens on.
    """
    def __init__(self, service):
        """
        :attr WebSocketService service: Reference to the top-level service.
        :attr EchoUpper protocol: The protocol this factor spawns.
        """
        self.service = service
        self.protocol = EchoUpper


class EchoUpper(Protocol):
    """
    Echo input back, upper-cased. Define your behaviors in here.
    """
    def dataReceived(self, data):
        log.msg("Got %r" % (data,))
        self.transport.write(data.upper())