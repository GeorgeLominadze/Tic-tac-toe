import random
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

winner = None
currentPlayer = 'X'
gameRunning = True


def printBoard(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(f'{board[6]}|{board[7]}|{board[8]}')


def playerInput(board):
    inp = int(input('Enter number 1-9:'))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = currentPlayer
    else:
        print('Oops the spot is already taken')


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != '-':
        board[6] = winner
        return True


def checkCol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != '-':
        board[2] = winner
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        board[0] = winner
        return True


def checkWin(board):
    global gameRunning
    if checkHorizontal(board) or checkCol(board) or checkDiag(board):
        printBoard(board)
        print(f'The winner is {winner}')
        gameRunning = False


def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print('It is a tie!')
        gameRunning = False


def switchPlayer(board):
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


def computer(board):
    while currentPlayer == 'O':
        pos = random.randint(1, 8)
        if board[pos] == '-':
            board[pos] = 'O'
            switchPlayer(board)


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer(board)
    computer(board)
    checkWin(board)
    checkTie(board)
