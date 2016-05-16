"""
multicodec
~~~~~~~~~~~~~~~~~~~~~


"""

import argparse
from abc import ABCMeta
import io.BufferedWriter
import io.BufferedReader

CODECS = [
            JSON,
            CBOR,
            PROTOBUF
         ]

def encode(codec, buf):
    if codec not in CODECS:
        raise InvalidCodecError

def decode(codec, buf):
    if codec not in CODECS:
        raise InvalidCodecError

class Codec(object):
    def __init__(self):
        self._header = None
        self._codec = None

        self._encoder = Encoder()
        self._decoder = Decoder()

    def encode(self, buf):
        self._encoder(buf) 

    def decode(self):
        self._decoder(buf)

class Encoder(io.BufferedWriter):
    """
    Multicodec encoder.
    
    :ivar _reader: Buffered write byte stream.
    """

    __metaclass__ = ABCMeta

    def __init__(self, writer):
        self._writer = writer

    @abstractmethod
    def __call__(self, buf):
        pass

class Decoder(io.BufferedReader):
    """
    Multicodec decoder.
    
    :ivar _reader: Buffered read byte stream.
    """

    __metaclass__ = ABCMeta

    def __init__(self, reader):
        self._reader = reader

    @abstractmethod
    def __call__(self):
        pass


def main():
    parser = argparse.ArgumentParser(description='A tool to inspect and manipulate mixed codec streams.')
    parser.add_argument("-e", "--encode", type=str
                        help="encode items to given codec")
    parser.add_argument("-d", "--decode", type=str
                        help="decode items of given codec")
    parser.add_argument("-v", "--verbose",
                        help="Increase verbosity", action="store_true")
    args = parser.parse_args()

def usage():
    pass

if __name__ == "__main__":
    main()
