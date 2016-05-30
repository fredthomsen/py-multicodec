"""
mutlicodec.coder_cbor
~~~~~~~~~~~~~~~~~~~~~

CBOR Multicodec encoder and decoder.
"""

from . import coder
from . import header
from . import exceptions

FORMAT = '/cbor/'


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

        pass


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

        pass
