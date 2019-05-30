

from enum import Enum

class JumpDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def displayChar(self):
        if self.value == 1:
            return 'U'
        elif self.value == 2:
            return 'D'
        elif self.value == 3:
            return 'L'
        elif self.value == 4:
            return 'R'
        return '?'
