"""
multicodec
~~~~~~~~~~~~~~~~~~~~~


"""

import argparse
from abc import ABCMeta

import multicodec.json
import multicodec.cbor
import multicodec.json
import multicodec.header

JSON_FORMAT = 'json'
CBOR_FORMAT = 'cbor'
PROTOBUF_FORMAT = 'protobuf'

CODEC_IMPLS = {
            JSON_FORMAT: (JSON_FORMAT, multicodec.json.Encoder, multicodec.json.Decoder),
            CBOR_FORMAT: (CBOR_FORMAT, multicodec.cbor.Encoder, multicodec.cbor.Decoder),
            PROTOBUF_FORMAT: (PROTOBUF_FORMAT, multicodec.protobuf.Encoder, multicodec.protobuf.Decoder),
         }


class MultiCodec(object):

    @staticmethod
    def build(codec):
        try:
            codec, encoderClass, decoderClass = CODEC_IMPLS[codec]
        except KeyError:
            raise InvalidCodecError
        mc = MultiCodec(codec, encoderClass, decoderClass)
       
    def __init__(self, codec, encoder, decoder):
        self._codec = codec
        self._encoder = encoder()
        self._decoder = decoder()

    def encode(self, buf):
        return self._encoder(buf) 

    def decode(self, buf):
        return self._decoder(buf)


def encode(codec, buf):
    mc = Multicodec.build(codec)
    return mc.encode(buf)


def decode(buf):
    codec = str(multicodec.header.read_header(buf))
    mc = Multicodec.build(codec)
    return mc.decode(buf)


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
