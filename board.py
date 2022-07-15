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
        if (self.tiles[x][y] == "E"):
            self.tiles[x][y] = cur
            print("valid move")
            self.draw()
        else:
            print("invalid move made")
