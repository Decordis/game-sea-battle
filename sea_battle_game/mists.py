class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "U\'re trying to shoot out of board! :(!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "U\'ve already shot here!"

class BoardWrongShipException(BoardException):
    pass
