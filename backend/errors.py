class MissingData(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class PlayListError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TokenError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message