"""
json
~~~~~~~~~~~~~~~~~~~~~


"""
import multicodec


class Encoder(multicodec.Encoder):
    def __call__(self, buf):
        pass


class Decoder(multicodec.Decoder):
    def __call__(self):
        pass
