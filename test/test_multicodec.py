"""
test.test_multicodec
~~~~~~~~~~~~~~~~~~~~~

Unit tests for multicodec.
"""

import cbor
import json
from hypothesis import strategies, given

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

mc_strategy = strategies.dictionaries(
    keys=strategies.text(
        alphabet='abcdefghijklmnopqrstuvwxyz1234567890',
        min_size=10),
    values=strategies.text(min_size=10),
    min_size=10, max_size=30)
@given(mc_dict=mc_strategy)
def test_rtt(mc_dict):
    assert decode(encode(JSON_FORMAT, json.dumps(mc_dict))) == {
            "codec": "json", "data": json.dumps(mc_dict)
    }


@given(mc_dict=mc_strategy)
def test_nested(mc_dict):
    json_str = json.dumps(mc_dict)
    json_mc_buf = encode(JSON_FORMAT, json_str)
    cbor_mc_buf = encode(CBOR_FORMAT, json_mc_buf)

    assert {'codec': 'cbor', 'data': {
        'codec': 'json', 'data': '{0}'.format(json_str)
    }} == decode(cbor_mc_buf)
