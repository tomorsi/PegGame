#!/usr/local/bin/python3.6

from PegState import PegState

class Matrix:

    WIDTH = 7
    HEIGHT = 7
    CORNER = 2

    def __init__(self):
        self.matrix = []

        for r in range(Matrix.HEIGHT):
            row = []
            for c in range(Matrix.WIDTH):
                if c < Matrix.CORNER and r < Matrix.CORNER:
                    row.append(PegState.NONE)
                elif c >= (Matrix.WIDTH - Matrix.CORNER) and r < Matrix.CORNER:
                    row.append(PegState.NONE)
                elif c < Matrix.CORNER and r >= (Matrix.HEIGHT - Matrix.CORNER):
                    row.append(PegState.NONE)
                elif c >= (Matrix.WIDTH - Matrix.CORNER) and r >= (Matrix.HEIGHT - Matrix.CORNER):
                    row.append(PegState.NONE)
                elif r == 3 and c == 4:
                    row.append(PegState.EMPTY)
                else:
                    row.append(PegState.FILLED)
            self.matrix.append(row)
        #self.display()
        #assert False

    def display(self):
        print("-----------------")
        for r in range(Matrix.HEIGHT):
            print("| ", end='')
            for c in range(Matrix.WIDTH):
                pegState = self.matrix[r][c]
                print(pegState.displayChar(),'',end='')
            print("|")
        print("-----------------")

    def state(self, r, c):
        return self.matrix[r][c]

    def setState(self, r, c, pegState):
        self.matrix[r][c] = pegState

    def valid(self, r, c):
        if c < Matrix.WIDTH and r < Matrix.HEIGHT and c > -1 and r > -1:
            return True
        return False
    
    def validColumn(self, c):
        if c > -1 and c < Matrix.WIDTH:
            return True
        return False

    def validRow(self, r):
        if r > -1 and r < Matrix.HEIGHT:
            return True
        return False

def main():
    matrix = Matrix()
    matrix.display()

if __name__ == '__main__':
    main()
