# Tic Tac Toe Game - 1 and 2 player mode
# In 1 player mode, user plays against the computer
# In 2 player mode, users take turns making a move
#
# Judith Gammie
# 22nd June 2-15

from random import randint
board = [ ['e' for i in range(3) ] for j in range(3)]

def single_player():
    print "Beginning game against the computer"
    while game_over() == 0:
        print_board()
        for i in range(0,9):
            if (i % 2 == 0):
                print "Player 1, make your move"
                x1, y1 = raw_input().split()
                x1, y1 = int(x1),int(y1)
                while (make_move(1, x1, y1) == 0):
                    print "Invalid move. Try again Player 1"
                    x1, y1 = raw_input().split()
                    x1, y1 = int(x1), int(y1)
                    if make_move(1,x1,y1) == 1:
                        break

            elif (i % 2 == 1):
                print "Computer will now make it's move"
                x2 = randint(0,2)
                y2 = randint(0,2)
                while (make_move(2, x2, y2) == 0):
                    x2 = randint(0,2)
                    y2 = randint(0,2)
                    if make_move(2,x2,y2) == 1:
                        break
 
            if (game_over() != 0):
                print "Game is over!"
                winner = game_over()
                if winner == 1:
                    print "Player 1 wins!"
                elif winner == 2:
                    print "Computer wins!"
                else: 
                    print "It's a tie!"
                quit()

def two_player():
    print "Two player game has begun"
    while game_over() == 0:
        print_board()
        for i in range(0,9):
            if (i % 2 == 0):
                print "Player 1, make your move"
                x1, y1 = raw_input().split()
                x1, y1 = int(x1),int(y1)
                while (make_move(1, x1, y1) == 0):
                    print "Invalid move. Try again Player 1"
                    x1, y1 = raw_input().split()
                    x1, y1 = int(x1), int(y1)
                    if make_move(1,x1,y1) == 1:
                        break

            elif (i % 2 == 1):
                print "Player 2, make your move"
                x2, y2 = raw_input().split()
                x2, y2 = int(x2), int(y2)
                while (make_move(2, x2, y2) == 0):
                    print "Invalid move. Try again Player 2"
                    x2, y2 = raw_input().split()
                    x2, y2 = int(x2), int(y2)
                    if make_move(2,x2,y2) == 1:
                        break
            if (game_over() != 0):
                print "Game is over!"
                winner = game_over()
                if winner == 1:
                    print "Player 1 wins!"
                elif winner == 2:
                    print "Player 2 wins!"
                else: 
                    print "It's a tie!"
                quit()

def print_board():
    print "   -----------"
    for y in range(2, -1, -1):
        print y,
        for x in range(3): print '|', board[x][y],  
        print '|'
        print "   -----------"
  #  print "----------"
    print "    0   1   2  "

def make_move(player, x, y):
    if (board[x][y] == 'e'):
        if player == 1:
            board[x][y] = 'X'
        elif player == 2:
            board[x][y] = 'O'
        print_board()
        return 1
    elif (board [x][y] != 'e'):
        return 0

def game_over():
    winner = 0
    # check for horizontal lines
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != 'e'):
            winner = 1 if board[i][0] == 'X' else 2

    # check for vertical lines
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] != 'e'):
            winner = 1 if board[0][i] == 'X' else 2

    # check for top to bottom diagonal
    if (board[0][0] == board[1][1] == board[2][2] != 'e'):
        winner = 1 if board[0][0] == 'X' else 2
    
    # check for botton to top diagonal
    elif (board[0][2] == board[1][1] == board[2][0] != 'e'):
        winner = 1 if board[0][2] == 'X' else 2
    
    #check if board full, no winner
    count = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] != 'e'):
                count = count + 1
    if count == 9:
        winner = 3 
    
    return winner

print "Welcome to Tic Tac Toe"
print "Enter 1 to play against the computer and 2 for 2 player mode"
num_players = raw_input()
num_players = int(num_players)

while (num_players != 1 and num_players != 2):
    print "Invalid input. Enter 1 for single player, 2 for two player"
    num_players = raw_input()
    num_players = int(num_players)

if num_players == 1:
    single_player()

elif num_players == 2:
    two_player()
