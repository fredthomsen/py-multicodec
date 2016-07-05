"""
multicodec.header
~~~~~~~~~~~~~~~~~~~~~

Module handles header creation, reading, and writing for multicodec buffers.
"""

import base64
import struct
from . import exceptions

MAX_PATH_LEN = 127


def header(path):
    """
    Creates header from path.

    :param path: Multicodec path.

    :return: header buffer.
    """

    path_len = len(path) + 1
    if path_len > MAX_PATH_LEN:
        raise exceptions.PathLenError

    pack_str = 'b{str_len}c'.format(str_len=len(path))
    byte_str_tuple = tuple([c.encode('utf-8') for c in path])
    buf = struct.pack(pack_str, path_len, *byte_str_tuple)
    buf += struct.pack('c', b'\n')

    return buf


def header_path(hdr):
    """
    Removes length and whitespace and returns the header path.

    :param path: Multicodec path.

    :return: header buffer.
    """

    try:
        path = hdr[1:].strip()
    except IndexError:
        raise exceptions.InvalidHeaderError

    return path


def add_header(buf, path):
    """
    Adds header to buffer.

    :param buf: Buffer with no header.
    :param path: Path to be written to header.

    :return: Buffer with header.
    """

    hdr = header(path)
    return b''.join([hdr, buf])


def get_header(buf):
    """
    Gets header from buffer

    :param buf: Multicodec buffer.

    :return: Header.
    """

    hdr, data = _split_header_contents(buf)
    hdr = hdr.decode('utf-8')
    hdr = hdr.strip('\n').strip('/')

    return hdr.encode('utf-8')


def rm_header(buf):
    """
    Strip header from buffer

    :param buf: Multicodec buffer.

    :return: Buffer without header.
    """

    hdr, data = _split_header_contents(buf)

    return data


def _split_header_contents(buf):
    """
    Splits buffer into header and data.

    :param buf: Multicodec buffer.

    :return: Header and content tuple.
    """

    try:
        hdr_len = struct.unpack('b', buf[0:1])[0]
    except IndexError:
        raise exceptions.InvalidHeaderError

    if hdr_len > MAX_PATH_LEN:
        raise exceptions.PathLenError

    hdr = buf[1:hdr_len + 1]
    data = buf[hdr_len + 1:]

    if hdr[0] == '\n':
        raise exceptions.InvalidHeaderError

    return hdr, data
