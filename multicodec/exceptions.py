"""
multicodec.exceptions
~~~~~~~~~~~~~~~~~~~~~

Classes for multicodec exceptions.
"""


class MultiCodecException(IOError):
    """
    Base multicodec exception.
    """

    pass


class InvalidCodecError(MultiCodecException, NotImplementedError):
    """
    Unimplemented codec error.
    """

    pass


class MalformedBufferError(MultiCodecException):
    """
    Malformed codec buffer error.
    """

    pass


class PathLenError(MultiCodecException):
    """
    Maximum path length exceeded.
    """


class InvalidHeaderError(MultiCodecException):
    """
    Invalid header error.
    """
