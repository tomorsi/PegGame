#!/usr/local/bin/python3.6


from Matrix import Matrix
from PegState import PegState
from JumpDirection import JumpDirection

class Mover:

    def __init__(self, matrix):
        self.matrix = matrix
        self.moves = 0

    # Direction can be up , down , left, right indicating
    # the direction of the jump 
    def move(self, r, c, dir):
        print(self.moves,". move(",r,",",c,",",dir.displayChar(),")", sep='')
        self.matrix.display()

        self.moves = self.moves + 1
        self.matrix.setState(r,c,PegState.FILLED)
        if dir == JumpDirection.DOWN:
            self.matrix.setState(r,r-1,PegState.EMPTY)
            self.matrix.setState(r,r-2,PegState.EMPTY)
            self.hasMove(r-1,c)
            self.hasMove(r-2,c)
        if dir == JumpDirection.UP:
            self.matrix.setState(r+1,c,PegState.EMPTY)
            self.matrix.setState(r+2,c,PegState.EMPTY)
            self.hasMove(r+1,c)
            self.hasMove(r+2,c)
        if dir == JumpDirection.RIGHT:
            self.matrix.setState(r,c-1,PegState.EMPTY)
            self.matrix.setState(r,c-2,PegState.EMPTY)
            self.hasMove(r,c-1)
            self.hasMove(r,c-2)
        if dir == JumpDirection.LEFT:
            self.matrix.setState(r,c+1,PegState.EMPTY)
            self.matrix.setState(r,c+2,PegState.EMPTY)
            self.hasMove(r,c+1)
            self.hasMove(r,c+2)

    # return the valid moves from a given point.
    def hasMove(self, r, c):
        if not self.matrix.valid(r,c):
            return
        if self.matrix.validColumn(c-2) and self.matrix.state(r,c-1) == PegState.FILLED and self.matrix.state(r,c-2) == PegState.FILLED:
            self.move(r,c,JumpDirection.RIGHT)
        if self.matrix.validColumn(c+2) and self.matrix.state(r,c+1) == PegState.FILLED and self.matrix.state(r,c+2) == PegState.FILLED:
            self.move(r,c,JumpDirection.LEFT)
        if self.matrix.validRow(r-2) and self.matrix.state(r-1,c) == PegState.FILLED and self.matrix.state(r-2,c) == PegState.FILLED:
            self.move(r,c,JumpDirection.DOWN)
        if self.matrix.validRow(r+2) and self.matrix.state(r+1,c) == PegState.FILLED and self.matrix.state(r+2,c) == PegState.FILLED:
            self.move(r,c,JumpDirection.UP)

def main():
    matrix = Matrix()
    mover = Mover(matrix)
    mover.hasMove(3,4)
    print("final")
    matrix.display()
    
    


if __name__ == '__main__':
    main()
