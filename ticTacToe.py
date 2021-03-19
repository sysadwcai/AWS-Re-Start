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


if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ':  # top row win
    printBoard(theBoard)
    print('Game Over')
    break
elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ':  # mid row win
    printBoard(theBoard)
    print('Game Over')
    break
elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ':  # low row win
    printBoard(theBoard)
    print('Game Over')
    break
elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ':  # diagonal win
    printBoard(theBoard)
    print('Game Over')
    break
elif theBoard['low-L'] == theBoard['mid-M'] == theBoard['top-R'] != ' ':  # diagonal win
    printBoard(theBoard)
    print('Game Over')
    break

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
