"""
multicodec.header
~~~~~~~~~~~~~~~~~~~~~

Module handles header creation, reading, and writing for multicodec buffers.
"""

import struct
from multicodec import exceptions

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

    buf = struct.pack('bsb', path_len, path, '\n')

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


def write_header(buf, path):
    """
    Adds header to buffer.

    :param buf: Buffer with no header.
    :param path: Path to be written to header.

    :return: Buffer with header.
    """

    hdr = header(path)
    return b''.join([hdr, buf])


def strip_header(buf):
    """
    Strip header from buffer

    :param buf: Multicodec buffer.

    :return: Buffer without header.
    """

    try:
        buf_len = buf[0]
    except IndexError:
        raise exceptions.InvalidHeaderError

    if buf_len > MAX_PATH_LEN:
        raise exceptions.PathLenError

    buf = buf[1:buf_len + 1]
    if buf[0] == '\n':
        raise exceptions.InvalidHeaderError

    return buf
