"""
test.test_json
~~~~~~~~~~~~~~~~~~~~~

Unit tests for JSON Multicdoec encoder and decoder.
"""

import json

from multicodec.coder_json import Encoder
from multicodec.coder_json import Decoder


def test_encoder():
    json_str = json.dumps({"hello": "world"})
    json_encoder = Encoder()

    assert json_encoder(json_str) == b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'


def test_decoder():
    json_mc_buf = b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'
    json_decoder = Decoder()

    assert json_decoder(json_mc_buf) == {"codec": "json", "data": '{"hello": "world"}'}
