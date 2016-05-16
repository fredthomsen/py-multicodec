"""
header
~~~~~~~~~~~~~~~~~~~~~


"""

import struct

MAX_PATH_LEN = 127


def header(path):
    path_len = len(path) + 1
    if path_len > MAX_PATH_LEN:
        raise PathLenError

    buf = struct.pack('bsb', path_len, path, '\n')

    return buf


def header_path(hdr):
    return str(hdr)[1:].strip()


def write_header(writer, path):
    hdr = header(path)
    return writer.write(hdr)


def read_header(reader):
    buf_len = reader.read(1)

    if buf_len > 127:
        raise PathLenError

    buf = reader.read(buf_len + 1)
    if buf[0] == '\n':
        raise HeaderInvalidError

    return buf_len + buf


def read_path(reader):
    hdr = read_header(reader)

    return header_path(hdr)


def consume_path(reader, path):
    buf = read_path(reader)
    if path != buf:
        raise HeaderMismatch


def consume_header(reader, header):
    buf = r.read(len(header))
    if path != buf:
        raise HeaderMismatch
