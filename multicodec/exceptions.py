"""
exceptions
~~~~~~~~~~~~~~~~~~~~~


"""

class MultiCodecException(IOError):
    """
    Base multicodec exception.
    """

    pass

class InvalidCodecError(MultiCodecException, NotImplementedError):
    """
    Unimplemented codec exception.
    """

    pass
