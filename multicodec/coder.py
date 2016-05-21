"""
coder
~~~~~~~~~~~~~~~~~~~~~


"""


class Encoder(object):
    """
    Multicodec encoder.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, buf):
        pass


class Decoder(object):
    """
    Multicodec decoder.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, buf):
        pass
