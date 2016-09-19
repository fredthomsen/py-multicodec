"""
test.test_multicodec
~~~~~~~~~~~~~~~~~~~~~

Unit tests for multicodec.
"""

import json
import cbor

from multicodec.multicodec import MultiCodec
from multicodec.multicodec import encode
from multicodec.multicodec import decode
from multicodec.multicodec import JSON_FORMAT, CBOR_FORMAT

from multicodec import coder_json


def test_build():
    json_mcoder = MultiCodec.build(JSON_FORMAT)
    assert ((json_mcoder._codec == JSON_FORMAT) and
            isinstance(json_mcoder._encoder, coder_json.Encoder) and
            isinstance(json_mcoder._decoder, coder_json.Decoder))


def test_encode():
    json_str = json.dumps({"hello": "world"})
    assert encode(JSON_FORMAT, json_str) == b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'


def test_decode():
    json_mc_buf = b'\x07\x2f\x6a\x73\x6f\x6e\x2f\x0a\x7b\x22\x68\x65\x6c\x6c\x6f\x22\x3a\x20\x22\x77\x6f\x72\x6c\x64\x22\x7d'
    assert decode(json_mc_buf) == {"codec": "json", "data": '{"hello": "world"}'}


def test_nested():
    json_str = json.dumps({"hello": "world"})
    json_mc_buf = encode(JSON_FORMAT, json_str)
    cbor_mc_buf = encode(CBOR_FORMAT, json_mc_buf)

    assert json_str == decode(cbor_mc_buf)
