"""
WebSocket Echo.

Install: pip install twisted txws

Run: twistd -ny server.tac

Open one of the HTML files under static/
"""
import time

from twisted.internet import reactor
from twisted.application import internet
from twisted.application.service import Application, Service

from txws import WebSocketFactory

from src.protocols.websockets import WebSocketServerFactory

class WebSocketService(Service):
    """
    A simple service that listens on port 8076 for WebSockets traffic.
    """
    def __init__(self):
        self.start_time = time.time()

    def start_service(self, application):
        """
        Gets the show on the road. Fires up a factory, binds the port.
        """
        echofactory = WebSocketServerFactory(self)
        factory = WebSocketFactory(echofactory)
        ws_server = internet.TCPServer(8076, factory)
        ws_server.setName('ws-tcp')
        ws_server.setServiceParent(application)

    def shutdown(self):
        """
        Gracefully shuts down the service.
        """
        reactor.callLater(0, reactor.stop)


# This is required for the 'twistd' command to be happy.
application = Application("ws-streamer")
ws_service = WebSocketService()
ws_service.start_service(application)

