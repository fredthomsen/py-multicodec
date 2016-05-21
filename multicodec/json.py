"""
json
~~~~~~~~~~~~~~~~~~~~~


"""
import json
import mutlicodec.coder
import multicodec.header

FORMAT = '/json/'

class Encoder(coder.Encoder):
    def __call__(self, buf):
        try:
            json.loads(buf)
        except ValueError:
            raise MalformedBufferError

        header.write_header(self._writer, FORMAT)

        return mc_buffer

class Decoder(coder.Decoder):
    def __call__(self, buf):
        header.
