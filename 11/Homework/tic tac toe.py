print("you can use numpad to put 'X' or 'O'")
board = ["_", "_","_",
        "_", "_", "_",
        "_", "_", "_"]
play=1
player_turn="O"
def clean():
    board = ["_", "_","_",
            "_", "_", "_",
            "_", "_", "_"]
move=[0,1,2,3,4,5,6,7,8]
def draw():
    print(" +-----+-----+-----+")
    print(" | ",board[0], " | ",board[1]," | ",board[2]," | ")
    print(" +-----+-----+-----+")
    print(" | ",board[3], " | ",board[4]," | ",board[5]," | ")
    print(" +-----+-----+-----+")
    print(" | ",board[6], " | ",board[7]," | ",board[8]," | ")
    print(" +-----+-----+-----+")
while play==1:
    def numToCell(num):
        if num>=7:
            return num-7
        elif num>=4:
            return num-1
        else:
            return num+5
    def win():
        if board[0]==board[1] and board[1]==board[2] and board[0]==player_turn:
            return player_turn
        if board[3]==board[4] and board[4]==board[5] and board[3]==player_turn:
            return player_turn
        if board[6]==board[7] and board[7]==board[8] and board[6]==player_turn:
            return player_turn
        if board[0]==board[3] and board[3]==board[6] and board[0]==player_turn:
            return player_turn
        if board[1]==board[4] and board[4]==board[7] and board[1]==player_turn:
            return player_turn
        if board[2]==board[5] and board[5]==board[8] and board[2]==player_turn:
            return player_turn
        if board[0]==board[4] and board[4]==board[8] and board[0]==player_turn:
            return player_turn
        if board[2]==board[4] and board[4]==board[6] and board[2]==player_turn:
            return player_turn
    print("Now is",player_turn)
    board[numToCell(int(input("chose")))]=player_turn
    draw()
    if win()=="O":
        print("The winner is",win())
        play=0
    elif win()=="X":
        print("The winner is",win())
        play=0
    if player_turn=="O":
        player_turn="X"
    elif player_turn=="X":
        player_turn="O"
    
