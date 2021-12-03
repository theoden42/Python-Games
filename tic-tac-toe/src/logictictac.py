class Game:

    def __init__(self: object) -> None:
        '''initialise the grid for a new game'''
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.sum_of_element = [[0,0,0], [0,0,0], [0,0]] 
        '''stores the sum of the elements in each row,
         each column and two diagonals'''

    def playmove(self: object, player: str, position: tuple) -> tuple[str, tuple]:  
        '''play a move and returns data of winning stroke if any player wins''' 
        X = position[0]
        Y = position[1]
        #update the list position if not already updated 
        if (self.grid[X][Y] != 0 or X not in range(0,3) or Y not in range(0,3)):
            return "INVALID_POSITION", (-1,-1)
        else:
            if (player == "zero") :
                val = 1
                self.grid[X][Y] = 1
            elif (player == "cross"):
                val = -1
                self.grid[X][Y] = -1
            else:
                return "INVALID_PLAYER", (-1, -1)
            self.sum_of_element[0][Y] += val #add -1 if cross moves and 1 if zero moves
            self.sum_of_element[1][X] += val

            if (X == 1 and Y == 1):
                self.sum_of_element[2][0] += val 
                self.sum_of_element[2][1] += val
            elif (X == Y):
                self.sum_of_element[2][0] += val
            elif (X + Y == 2):
                self.sum_of_element[2][1] += val
            
            win = self.checkwin()
            if(win[0] == 1):
                return "ZERO_WINS", win
            elif (win[0 == -1]):
                return "CROSS_WINS", win
            else:
                return "CONTINUE", win

    def checkwin(self) -> tuple:
        if (3 in self.sum_of_element[0]):
            return (1, 0, self.sum_of_element[0].index(3))
        elif (3 in self.sum_of_element[1]):
            return (1, 1, self.sum_of_element[1].index(3))
        elif (3 in self.sum_of_element[2]):
            return (1, 2, self.sum_of_element[2].index(3))
        elif (-3 in self.sum_of_element[0]):
            return (-1, 0, self.sum_of_element[0].index(-3))
        elif (-3 in self.sum_of_element[1]):
            return (-1, 1, self.sum_of_element[1].index(-3))
        elif (-3 in self.sum_of_element[2]):
            return (-1, 2, self.sum_of_element[2].index(-3))
        else :
            return (0,-1,-1)


if __name__ == "__main__":
    print("please call from main.py")
    