"""
test.test_multicodec
~~~~~~~~~~~~~~~~~~~~~

Unit tests for multicodec.
"""

import cbor
import json
from hypothesis import strategies, given
import pytest

from multicodec.multicodec import MultiCodec
from multicodec.multicodec import encode
from multicodec.multicodec import decode
from multicodec.multicodec import JSON_FORMAT, CBOR_FORMAT
from multicodec import coder_json, coder_cbor


@pytest.mark.parametrize('mc_format, coder', [
    (JSON_FORMAT, coder_json),
    (CBOR_FORMAT, coder_cbor)
    ])
def test_build(mc_format, coder):
    mcoder = MultiCodec.build(mc_format)
    assert ((mcoder._codec == mc_format) and
            isinstance(mcoder._encoder, coder.Encoder) and
            isinstance(mcoder._decoder, coder.Decoder))

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
