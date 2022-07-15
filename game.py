from board import Board

b = Board()
b.draw()

##b.playMove(0, 0, "X")
##b.playMove(0, 0, "O")

inputX = int(input("What row would you like to play your move? "))
inputY = int(input("What column would you like to play your move? "))

b.playMove(inputX, inputY, "X")
