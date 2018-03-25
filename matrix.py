# This class provides basic operation on one Matrix

import sys

class oneMatrix:

    def __init__(self, cols, rows):
        self.Matrix = [[0 for x in range(cols)] for y in range(rows)]
    
    def rows(self):
        return len(self.Matrix)

    def cols(self):
        return len(self.Matrix[0])        

    def Print(self):
        for x in range(0,self.rows):
            line = ""
            for y in range(0,self.cols):
                line += str(self.Matrix[x][y]) + "| "
            line += "\n"
            print(line)


A = oneMatrix(3,3)
A.Print()
            
        