"""
test.test_cbor
~~~~~~~~~~~~~~~~~~~~~

Unit tests for CBOR Multicdoec encoder and decoder.
"""

import cbor

from multicodec.coder_cbor import Encoder
from multicodec.coder_cbor import Decoder


def test_encoder():
    cbor_str = cbor.dumps({"hello": "world"})
    cbor_encoder = Encoder()

    assert cbor_encoder(cbor_str) == b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'


def test_decoder():
    cbor_mc_buf = b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'
    cbor_decoder = Decoder()

    assert cbor_decoder(cbor_mc_buf) == {"codec": "cbor", "data": '{"hello": "world"}'}
