# CUSTOM
class InvalidArgument(Exception):
    pass

class MissingArgument(Exception):
    pass

# HTTP
class BadRequest(Exception): # 400
    pass

class NotFound(Exception): # 404
    pass

class TooManyRequests(Exception): # 429
    pass

class UnknownError(Exception):
    pass
