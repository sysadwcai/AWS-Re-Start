# Create a tic tac toe game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


while board['top-L'] + board['top-M'] + board['top-R'] != 'X' or
board['mid-L'] + board['mid-M'] + board['mid-R'] != 'X' or
board['low-L'] + board['low-M'] + board['low-R'] != 'X' or
board['top-L'] + board['top-M'] + board['top-R'] != 'O' or
board['mid-L'] + board['mid-M'] + board['mid-R'] != 'O' or
board['low-L'] + board['low-M'] + board['low-R'] != 'O' or
board['top-L'] + board['mid-M'] + board['low-R'] != 'X' or
board['low-L'] + board['mid-M'] + board['top-R'] != 'X' or
board['top-L'] + board['mid-M'] + board['low-R'] != 'O' or
board['low-L'] + board['mid-M'] + board['top-R'] != 'O'
# test

turn = 'X'  # X goes first
for i in range(9):  # There are only 9 moves in the game
    printBoard(theBoard)  # initialize the empty board
    print('Turn for ' + turn + '. Move on which space?')
    move = input()  # prompting player input
    theBoard[move] = turn
    if turn == 'X':  # Player take turn to enter input
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
