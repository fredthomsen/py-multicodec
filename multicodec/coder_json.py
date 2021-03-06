"""
mutlicodec.coder_json
~~~~~~~~~~~~~~~~~~~~~

JSON Multicodec encoder and decoder.
"""

import json
import copy

from . import coder
from . import header
from . import exceptions

FORMAT = '/json/'
DECODED_DICT_FMT = {"codec": "json", "data": ""}


class Encoder(coder.Encoder):
    """
    JSON Encoder.
    """

    def __call__(self, buf):
        """
        JSON Multicodec encoder functionality.

        :params buf: JSON string.

        :return: JSON Multicodec buffer.
        """

        try:
            json.loads(buf)
        except ValueError:
            raise exceptions.MalformedBufferError

        encoded = header.add_header(buf.encode('utf-8'), FORMAT)
        return encoded


class Decoder(coder.Decoder):
    """
    JSON Decoder.
    """

    def __call__(self, buf):
        """
        JSON Multicodec decoder functionality.

        :params buf: JSON multicodec buffer.

        :return: Dictionary containing JSON string.
        """

        buf = header.rm_header(buf)
        decoded = copy.copy(DECODED_DICT_FMT)
        decoded['data'] = buf.decode('utf-8')

        return decoded
