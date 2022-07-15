class Board:
    tiles = []
    
    def __init__(self):
        print("Board Initialized with size (8, 8)")

    def createBoard(self):
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")
        self.tiles.append("x")

    def draw(self):
        for i in range(len(self.tiles)):
            print("[]")
