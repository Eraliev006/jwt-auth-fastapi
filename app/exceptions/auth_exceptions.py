class ExpireSignatureError(Exception):
    pass

class InvalidTokenError(Exception):
    pass

class InvalidSignatureError(Exception):
    pass

class PasswordIsIncorrect(Exception):
    pass

class UserNotVerifyEmail(Exception):
    pass

class InvalidTokenType(Exception):
    pass

class RefreshTokenIsNotExists(Exception):
    pass