"""
test.test_json
~~~~~~~~~~~~~~~~~~~~~

Unit tests for JSON Multicdoec encoder and decoder.
"""

import json
from hypothesis import strategies, given

from multicodec.coder_json import Encoder
from multicodec.coder_json import Decoder

encoder = Encoder()
decoder = Decoder()

@given(mc_dict=strategies.dictionaries(
    keys=strategies.text(
        alphabet='abcdefghijklmnopqrstuvwxyz1234567890',
        min_size=10),
    values=strategies.text(min_size=10),
    average_size=15)
)
def test_rtt(mc_dict):
    assert decoder(encoder(json.dumps(mc_dict))) == {
            "codec": "json", "data": json.dumps(mc_dict)
    }
