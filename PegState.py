

from enum import Enum

class PegState(Enum):
    NONE = 1
    EMPTY = 2
    FILLED = 3

    def displayChar(self):
        if self.value == 1:
            return 'X'
        elif self.value == 2:
            return 'O'
        elif self.value == 3:
            return 'I'
        return '?'

