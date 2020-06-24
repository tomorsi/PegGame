#!/usr/local/bin/python3.6

from copy import deepcopy
from Matrix import Matrix
from PegState import PegState
from JumpDirection import JumpDirection

class Mover:

    def __init__(self, matrix):
        self.matrix = matrix
        self.moves = 0

    # Direction can be up , down , left, right indicating
    # the direction of the jump 
    def move(self, r, c, dir, matrix):
        Matrix.MATRIX = Matrix.MATRIX + 1

        print(Matrix.MATRIX,":",matrix.moves,". move(",r,",",c,",",dir.displayChar(),")", sep='')
        matrix.display()

        matrix.move()
        matrix.setState(r,c,PegState.FILLED)
        if dir == JumpDirection.DOWN:
            matrix.setState(r-1,c,PegState.EMPTY)
            matrix.setState(r-2,c,PegState.EMPTY)
            pegs = matrix.removePeg()
            if pegs > 1:
                self.hasMove(r-1,c,matrix)
                self.hasMove(r-2,c,matrix)
            else:
                if r == 3 and c == 3:
                    print("SOLVED")
                    assert False
        if dir == JumpDirection.UP:
            matrix.setState(r+1,c,PegState.EMPTY)
            matrix.setState(r+2,c,PegState.EMPTY)
            pegs = matrix.removePeg()
            if pegs > 1:
                self.hasMove(r+1,c,matrix)
                self.hasMove(r+2,c,matrix)
            else:
                if r == 3 and c == 3:
                    print("SOLVED")
                    assert False
        if dir == JumpDirection.RIGHT:
            matrix.setState(r,c-1,PegState.EMPTY)
            matrix.setState(r,c-2,PegState.EMPTY)
            pegs = matrix.removePeg()
            if pegs > 1:
                self.hasMove(r,c-1,matrix)
                self.hasMove(r,c-2,matrix)
            else:
                if r == 3 and c == 3:
                    print("SOLVED")
                    assert False
        if dir == JumpDirection.LEFT:
            matrix.setState(r,c+1,PegState.EMPTY)
            matrix.setState(r,c+2,PegState.EMPTY)
            pegs = matrix.removePeg()
            if pegs > 1:
                self.hasMove(r,c+1,matrix)
                self.hasMove(r,c+2,matrix)
            else:
                if r == 3 and c == 3:
                    print("SOLVED")
                    assert False

    # return the valid moves from a given point.
    def hasMove(self, r, c,matrix):
        if not self.matrix.valid(r,c):
            print("location: ",r,c, "not valid")
            return

        if matrix.validColumn(c-2) and matrix.state(r,c-1) == PegState.FILLED and matrix.state(r,c-2) == PegState.FILLED:
            copyMatrix = deepcopy(matrix)
            self.move(r,c,JumpDirection.RIGHT,copyMatrix)
        if matrix.validColumn(c+2) and matrix.state(r,c+1) == PegState.FILLED and matrix.state(r,c+2) == PegState.FILLED:
            copyMatrix = deepcopy(matrix)
            self.move(r,c,JumpDirection.LEFT,copyMatrix)
        if matrix.validRow(r-2) and matrix.state(r-1,c) == PegState.FILLED and matrix.state(r-2,c) == PegState.FILLED:
            copyMatrix = deepcopy(matrix)
            self.move(r,c,JumpDirection.DOWN,copyMatrix)
        if matrix.validRow(r+2) and matrix.state(r+1,c) == PegState.FILLED and matrix.state(r+2,c) == PegState.FILLED:
            copyMatrix = deepcopy(matrix)
            self.move(r,c,JumpDirection.UP,copyMatrix)
        print("location: ",r,c, "no move")

    def start(self):
        self.hasMove(2, 2, self.matrix)

def main():
    matrix = Matrix()
    mover = Mover(matrix)
    mover.start()
    print("final")
    matrix.display()
    
    


if __name__ == '__main__':
    main()
