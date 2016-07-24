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

    assert cbor_encoder(cbor_str) == \
        b'\x07\x2f\x63\x62\x6f\x72\x2f\x0a\xa1EhelloEworld'


def test_decoder():
    cbor_mc_buf = b'\x07\x2f\x63\x62\x6f\x72\x2f\x0a\xa1EhelloEworld'
    cbor_decoder = Decoder()

    assert cbor_decoder(cbor_mc_buf) == {
        "codec": "cbor",
        "data": b'\xa1EhelloEworld'
    }
