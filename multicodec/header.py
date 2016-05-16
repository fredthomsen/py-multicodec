"
header
~~~~~~~~~~~~~~~~~~~~~


"""

import struct

MAX_BUF_LEN = 127


def header(path):
    path_len = len(path) + 1
    if path_len >= 127:
        raise PathLenError

    buf = struct.pack('bsb', path_len, path, '\n')

    return buf


def header_path(hdr):
    return str(hdr)[1:].strip()


def write_header(writer, path):
    hdr = header(path)
    return writer.write(hdr)


def read_header(reader):
    buf = reader.read(1)
    buf_len = buf

    if buf_len > 127:
        raise
