"""
This module contains all the exceptions used in pyngid
"""

class PyngidException(Exception):
    """Base exception class for pyngid"""
    pass

class PyngidRuntimeError(PyngidException):
    """Raised when a runtime error occurs"""
    pass

class PyngidValueError(PyngidException):
    """Raised when a value error occurs"""
    pass

class PyngidUnsupportedError(PyngidException):
    """Raised when an unsupported feature is used"""
    pass