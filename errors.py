class Error_custom(Exception):
    """Base class for custom errors"""
    pass

# These errors are built to be "raised" using the raise keyword, not handled by a dev!
# DONT "HANDLE" THESE ERRORS USING `try` `except` `else`!

class NotDownloadedError(Error_custom):
    """Raised when a required download has not been completed"""
    pass

class InvalidInputError(Error_custom):
    """Raised when the input value is invalid"""
    pass

class ReasonedTimeoutError(Error_custom):
    """Raised when an operation times out with a reason"""
    pass

class CustomMaxValueError(Error_custom):
    """Raised when a custom maximum value is exceeded"""
    pass

class TimeoutError(Error_custom):
    """Raised when an operation times out"""
    pass

class ConnectionError(Error_custom):
    """Raised when a connection fails (especially for IoT projects)"""
    pass

class FailedOperationError(Error_custom):
    """Raised when an operation fails"""
    pass

#I'D RATHER SLEEP THAN STAY AWAKE X BRAZILLIAN FUNK 

class Ghost__Error(Error_custom):
    pass
#idk rasie this error when you bored or smth idk 










