"""
mutlicodec.coder_protobuf
~~~~~~~~~~~~~~~~~~~~~

Protobuf Multicodec encoder and decoder.
"""

import copy

from google import protobuf

from . import coder
from . import header
from . import exceptions

FORMAT = '/protobuf/'
DECODED_DICT_FMT = {"codec": "protobuf", "data": ""}


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

        buf = header.rm_header(buf)
        decoded = copy.copy(DECODED_DICT_FMT)
        decoded['data'] = buf.decode('utf-8')

        return decoded
