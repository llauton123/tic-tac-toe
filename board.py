import random

class Board:
    size = 3
    tiles = [[], [], []]
    
    def __init__(self):
        self.createBoard()
        print("Board Initialized with size (3, 3)")

    def createBoard(self):        
        self.tiles[0].append("E")
        self.tiles[0].append("E")
        self.tiles[0].append("E")
        self.tiles[1].append("E")
        self.tiles[1].append("E")
        self.tiles[1].append("E")
        self.tiles[2].append("E")
        self.tiles[2].append("E")
        self.tiles[2].append("E")

    def draw(self):
        for i in self.tiles:
            for j in i:
                print(j, end = " ")
            print()

    def playMove(self, x, y, cur):
        if (x > self.size) or (y > self.size):
            print("invalid selection made")
            return False
        if (self.tiles[x - 1][y - 1] == "E"):
            self.tiles[x - 1][y - 1] = cur
            print("valid move")
            self.draw()
            return True
        else:
            print("invalid move made")
            return False

    def playAIMove(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if (self.tiles[row][col] == "X"):
            self.playAIMove()
        else:
            self.tiles[row][col] = "O"
        
        print("Move made")
        self.draw()

    def checkWinningConditions(self):
        print("Winner determined")

        winningConditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                             [1, 4, 7], [2, 5, 8], [3, 6, 9],
                             [1, 5, 9], [3, 5, 7]]
