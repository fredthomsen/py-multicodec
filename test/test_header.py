"""
test.test_header
~~~~~~~~~~~~~~~~~~~~~

Unit tests for header module.
"""

from multicodec.header import header
from multicodec.header import header_path
from multicodec.header import add_header
from multicodec.header import rm_header
from multicodec.header import get_header


def test_header():
    test_hdr = '/my/test'
    expected = b'\x09\x2f\x6d\x79\x2f\x74\x65\x73\x74\x0a'
    assert header(test_hdr) == expected


def test_header_path():
    header = b'\x08\x2f\x6d\x79\x2f\x74\x65\x73\x74\x0a'
    expected = b'\x2f\x6d\x79\x2f\x74\x65\x73\x74'
    assert header_path(header) == expected


def test_add_header():
    buf = b'\x01\x02\x03\x04'
    path = '/test/'
    expected = b'\x07\x2f\x74\x65\x73\x74\x2f\x0a\x01\x02\x03\x04'
    assert add_header(buf, path) == expected


def test_rm_header():
    buf = b'\x07\x2f\x74\x65\x73\x74\x2f\x0a\x01\x02\x03\x04'
    expected = b'\x01\x02\x03\x04'
    assert rm_header(buf) == expected


def test_get_header():
    buf = b'\x07\x2f\x74\x65\x73\x74\x2f\x0a\x01\x02\x03\x04'
    expected = 'test'
    assert get_header(buf) == expected
