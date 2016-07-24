"""
mutlicodec.coder_cbor
~~~~~~~~~~~~~~~~~~~~~

CBOR Multicodec encoder and decoder.
"""

import cbor
import copy

from . import coder
from . import header
from . import exceptions

FORMAT = '/cbor/'
DECODED_DICT_FMT = {"codec": "cbor", "data": ""}


class Encoder(coder.Encoder):
    """
    CBOR Encoder.
    """

    def __call__(self, buf):
        """
        CBOR Multicodec encoder functionality.

        :params buf: CBOR string.

        :return: CBOR Multicodec buffer.
        """

        try:
            cbor.loads(buf)
        except (ValueError, EOFError):
            raise exceptions.MalformedBufferError

        encoded = header.add_header(buf, FORMAT)
        return encoded


class Decoder(coder.Decoder):
    """
    CBOR Decoder.
    """

    def __call__(self, buf):
        """
        CBOR Multicodec decoder functionality.

        :params buf: CBOR multicodec buffer.

        :return: Dictionary containing CBOR string.
        """

        buf = header.rm_header(buf)
        decoded = copy.copy(DECODED_DICT_FMT)
        decoded['data'] = buf

        return decoded
