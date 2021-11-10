import json
from websocket import create_connection
import typing


class SocketClient:
    """
    This class provides a connection to the coinbase websocket feed.
    Note: I used an external websocket-client library here because I couldn't figure out
    how to specify the wss protocol in the built-in python socket library.
    """

    def __init__(self, host: str, subscribe_msg: dict) -> None:
        """
        :param host: The websocket feed endpoint address which was specified in the api documentation.
        :param subscribe_msg: The subscription message which was specified in the api documentation.
        """
        self.connection = create_connection(host)
        self.subscribe_msg = subscribe_msg

    def send_msg(self, message: dict) -> None:
        """
        Converts any message to JSON format and sends it to the websocket API.
        :param message: Should be a dict as the API only accepts JSON defined in the documentation.
        """
        self.connection.send(json.dumps(message))

    def receive_msg(self) -> dict:
        """
        Receives a message from the websocket API and converts it to python native data type.
        :return: Should be a dict as the API only sends JSON defined in the documentation.
        """
        return json.loads(self.connection.recv())

    def subscription_generator(self) -> typing.Generator[dict, None, None]:
        """
        Generates each required format message received.
        :return: Generator object
        """
        self.send_msg(self.subscribe_msg)
        while True:
            if self.receive_msg().get('type') == 'match':
                yield self.receive_msg()
