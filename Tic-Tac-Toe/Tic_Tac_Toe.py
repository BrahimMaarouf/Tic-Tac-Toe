import os
from re import A
demo = [ 1, 2, 3, 4, 5, 6, 7, 8, 9] #position to put X/Y
test = [ '', '', '', '', '', '', '', '', '']

player1_choices = []
player2_choices = []

win_cond = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

def tic_ui(ui):
    print(" ___________")
    print(f"| {ui[0]} | {ui[1]} | {ui[2]} |")
    print(" ---+---+---")
    print(f"| {ui[3]} | {ui[4]} | {ui[5]} |")
    print(" ---+---+---")
    print(f"| {ui[6]} | {ui[7]} | {ui[8]} |")
    print(" ---+---+---")
    return 0

class Player:  #this is my players identifier player 1; choice : X or Y
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

def inputValidation(n):
    while n > 9  or n < 1 or test[n - 1] == 'X' or test[n - 1] == 'Y':
        n = int(input())
    return n

def gameLogic(p1, p2):

    for condition in win_cond:

        if all(pos in player1_choices for pos in condition):
            print(f"{p1.name} Wins!")
            exit(0)

    for condition in win_cond:
        if all(pos in player2_choices for pos in condition):
            print(f"{p2.name} Wins!")
            exit(0)

def tic_tac_toe():
    tic_ui(demo)
    player1 = Player("Player 1", 'X')
    player2 = Player("Player 2", 'Y')

    lock = 1 # i did this to know wich one is turn player1 or player2 ^^

    for i in range(1,len(test) + 1 ):
        if lock == 1 : #we in player 1
            pos1 = int(input("Player 1 input ? "))
            pos1 = inputValidation(pos1)
            player1_choices.append(pos1)
            test[pos1 -1] = player1.choice
            os.system('cls')
            tic_ui(test)
            gameLogic(player1, player2)
            lock = 0
        else :
            pos2 = int(input("Player 2 input ? "))
            pos2 = inputValidation(pos2)
            player2_choices.append(pos2)
            test[pos2 - 1] = player2.choice
            os.system('cls')
            tic_ui(test)
            gameLogic(player1, player2)
            lock = 1

        
# Run the game

tic_tac_toe()
