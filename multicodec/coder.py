"""
multicodec.coder
~~~~~~~~~~~~~~~~~~~~~

Abstract classes defining encoder and decoder.
"""

from abc import ABCMeta
from abc import abstractmethod


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
