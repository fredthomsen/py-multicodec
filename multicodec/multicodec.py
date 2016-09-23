"""
multicodec.multicodec
~~~~~~~~~~~~~~~~~~~~~

Main multicodec module.
"""

import argparse

from . import header
from . import exceptions
from . import coder_json
from . import coder_cbor
#from . import coder_protobuf

from . import __version__

JSON_FORMAT = 'json'
CBOR_FORMAT = 'cbor'
#PROTOBUF_FORMAT = 'protobuf'

# TODO: Move to metaclass for coder classes as suggested
CODEC_IMPLS = {
            JSON_FORMAT: (JSON_FORMAT, coder_json.Encoder, coder_json.Decoder),
            CBOR_FORMAT: (CBOR_FORMAT, coder_cbor.Encoder, coder_cbor.Decoder),
#            PROTOBUF_FORMAT: (PROTOBUF_FORMAT, multicodec.protobuf.Encoder, multicodec.protobuf.Decoder),
         }

class MultiCodec(object):

    @staticmethod
    def build(codec):
        try:
            codec, encoderClass, decoderClass = CODEC_IMPLS[codec]
        except KeyError:
            raise exceptions.InvalidCodecError
        return MultiCodec(codec, encoderClass, decoderClass)

    def __init__(self, codec, encoder, decoder):
        self._codec = codec
        self._encoder = encoder()
        self._decoder = decoder()

    def encode(self, buf):
        return self._encoder(buf)

    def decode(self, buf):
        return self._decoder(buf)

    @property
    def codec(self):
        return self._codec


def encode(codec, buf):
    mc = MultiCodec.build(codec)
    return mc.encode(buf)


def decode(buf):

    codecs = []
    done = False

    while not done:
        if type(buf) is dict:
            buf = buf['data']
        try:
            codec = str(header.get_header(buf))
            mc = MultiCodec.build(codec)
        except (exceptions.InvalidHeaderError, exceptions.InvalidCodecError):
            done = True
        else:
            codecs.append(codec)
            buf = mc.decode(buf)

    while codecs:
        codec = codecs.pop()
        buf = {'codec': codec, 'data': buf}

    return buf


def main():
    parser = argparse.ArgumentParser(description='A tool to inspect and manipulate mixed codec streams.')
    parser.add_argument("-e", "--encode", action='store', type=str,
                        help="Encode item to given codec")
    parser.add_argument("-c", "--codec", action='store', type=str,
                        help="Codec for use with encoding")
    parser.add_argument("-d", "--decode", help="Decode item")
    parser.add_argument("-v", "--version", action='version',
                        version=__version__)

    args = parser.parse_args()

    if args.encode and args.codec:
        print(encode(args.codec, args.encode))
    elif args.decode:
        print (decode(args.decode))

if __name__ == "__main__":
    main()
