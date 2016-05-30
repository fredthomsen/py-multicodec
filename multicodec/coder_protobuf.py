"""
mutlicodec.coder_protobuf
~~~~~~~~~~~~~~~~~~~~~

Protobuf Multicodec encoder and decoder.
"""

from . import coder
from . import header
from . import exceptions

FORMAT = '/protobuf/'


class Encoder(coder.Encoder):
    """
    Protobuf Encoder.
    """

    def __call__(self, buf):
        """
        Protobuf Multicodec encoder functionality.

        :params buf: protobuf string.

        :return: protobuf Multicodec buffer.
        """

        pass


class Decoder(coder.Decoder):
    """
    Protobuf Decoder.
    """

    def __call__(self, buf):
        """
        Protobuf Multicodec decoder functionality.

        :params buf: protobuf multicodec buffer.

        :return: Dictionary containing protobuf string.
        """

        pass
