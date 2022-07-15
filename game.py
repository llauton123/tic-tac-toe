from board import Board

b = Board()
b.draw()

##b.playMove(0, 0, "X")
##b.playMove(0, 0, "O")

print("If you would like to place a X in row 1, 1." + 
      "For each of the following, type 1 respectively. A general rule is that row n, column n will be the nth spot on the grid.")

while (True):
    inputX = int(input("What row would you like to play your move? "))
    inputY = int(input("What column would you like to play your move? "))

    b.playMove(inputX, inputY, "X")

    print("Opponent playing move...")
    b.playAIMove()
