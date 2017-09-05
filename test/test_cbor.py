"""
test.test_cbor
~~~~~~~~~~~~~~~~~~~~~

Unit tests for CBOR Multicdoec encoder and decoder.
"""

import cbor
from hypothesis import strategies, given

from multicodec.coder_cbor import Encoder
from multicodec.coder_cbor import Decoder

encoder = Encoder()
decoder = Decoder()

@given(mc_dict=strategies.dictionaries(
    keys=strategies.text(
        alphabet='abcdefghijklmnopqrstuvwxyz1234567890',
        min_size=10),
    values=strategies.text(min_size=10),
    average_size=10)
)
def test_rtt(mc_dict):
    assert decoder(encoder(cbor.dumps(mc_dict))) == {
            "codec": "cbor", "data": cbor.dumps(mc_dict)
    }
