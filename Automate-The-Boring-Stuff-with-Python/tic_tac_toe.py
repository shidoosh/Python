import pprint
import random



theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
letters = ['X', 'O']


def clearBoard(board):
    for move in board.keys():
        board[move] = ' '

def printBoard(board):
    print('   ' + board['top-L'] + '   ' + '|' + '   ' + board['top-M'] + '   ' + '|' + '   ' + board['top-R'] + '   ')
    print('-----------------------')
    print('   ' + board['mid-L'] + '   ' + '|' + '   ' + board['mid-M'] + '   ' + '|' + '   ' + board['mid-R'] + '   ')
    print('-----------------------')
    print('   ' + board['low-L'] + '   ' + '|' + '   ' + board['low-M'] + '   ' + '|' + '   ' + board['low-R'] + '   ')

def printKey(board):
    print(' top-L ' + '|' + ' top-M ' + '|' + ' top-R ')
    print('-----------------------')
    print(' mid-L ' + '|' + ' mid-M ' + '|' + ' mid-R ')
    print('-----------------------')
    print(' low-L ' + '|' + ' low-M ' + '|' + ' low-R ')


def assignLetter(letter):
    global thePlayer
    global theCPU

    while letter not in letters:
        print('Only X or O is allowed. Please try again.')
        letter = str(input().upper())

    if letter == 'X':
        thePlayer = 'X'
        theCPU = 'O'
    elif letter == 'O':
        thePlayer = 'O'
        theCPU = 'X'

def isFull(board):
    # check if cat's game
    if ' ' in board.values():
        return False
    else:
        return True

# Player Moves

def makePlayerMove(move, board):
    # checks for invalid input where the move doesn't exist
    while move not in board:
        print('Please enter one of the moves listed exactly as shown.')
        move = input()
    # checks for invalid input where the space is already taken
    while board[move] != ' ':
        print('This space is taken, please enter your move on an available space.')
        move = input()

    board[move] = thePlayer



def playerThreeInARow(board):
    if board['top-L'] == thePlayer and board['top-L'] == board['top-M'] and board['top-M'] == board['top-R']:
            return True

    elif board['mid-L'] == thePlayer and board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R']:
            return True

    elif board['low-L'] == thePlayer and board['low-L'] == board['low-M'] and board['low-M'] == board['low-R']:
            return True

    else:
        return False

def playerThreeInAColumn(board):
    if board['top-L'] == thePlayer and board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L']:
            return True

    elif board['top-M'] == thePlayer and board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M']:
            return True

    elif board['top-R'] == thePlayer and board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R']:
            return True

    else:
        return False


def playerThreeInADiag(board):
    if board['top-L'] == thePlayer and board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R']:
        return True

    if board['low-L'] == thePlayer and board['low-L'] == board['mid-M'] and board['mid-M'] == board['top-R']:
        return True

    else:
        return False


def playerWon(board):
    if playerThreeInARow(board) or playerThreeInAColumn(board) or playerThreeInADiag(board):
        return True
    else:
        return False






# CPU Moves
def trivial_makeCPUMove(board):
    # really dumb, just fills next empty space
    for m, l in board.items():
        if l == ' ':
            board[m] = theCPU
            break

def random_makeCPUMove(board):
    randomChoice = random.choice(list(board.items())) # tuple

    while randomChoice[1] != ' ': # choice needs to be empty spot on the board
        randomChoice = random.choice(list(board.items()))

    board[randomChoice[0]] = theCPU

# TODO:
# make smart CPU move
# def smart_makeCPUMove(board)
# check first for player's two in a row, if exists, block
# if does not exist, check CPU two in a row. if doesn't exist make CPU two in a row if empty space near CPU's previous move.
# if not, make random move


def CPUThreeInARow(board):
    if board['top-L'] == theCPU and board['top-L'] == board['top-M'] and board['top-M'] == board['top-R']:
            return True

    elif board['mid-L'] == theCPU and board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R']:
            return True

    elif board['low-L'] == theCPU and board['low-L'] == board['low-M'] and board['low-M'] == board['low-R']:
            return True

    else:
        return False


def CPUThreeInAColumn(board):
    if board['top-L'] == theCPU and board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L']:
            return True

    elif board['top-M'] == theCPU and board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M']:
            return True

    elif board['top-R'] == theCPU and board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R']:
            return True

    else:
        return False

def CPUThreeInADiag(board):
    if board['top-L'] == theCPU and board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R']:
        return True

    if board['low-L'] == theCPU and board['low-L'] == board['mid-M'] and board['mid-M'] == board['top-R']:
        return True

    else:
        return False

def CPUWon(board):
    if CPUThreeInARow(board) or CPUThreeInAColumn(board) or CPUThreeInADiag(board):
        return True
    else:
        return False


def playAgain(board):
    print('Play again? (y/n)')
    yes_or_no = ['Y', 'N']
    i = input().upper()
    while i not in yes_or_no:
        print('Please enter \'y\' to play again or \'n\' to quit')
        i = input().upper()

    if i == 'Y':
        clearBoard(board)
        playGame()
    else:
        print('GGs!')
        exit()

def postGame(result, board):
    printBoard(board)

    if result == 'player':
        print('You won!')

    elif result == 'cpu':
        print('I won!')

    else:
        print('Aw, cat\'s game! Better luck next time!')

    playAgain(board)


def playGame():

    print('Let\'s play Tic-Tac-Toe!')
    printBoard(theBoard)

    print('Type X or O to play')
    assignLetter(str(input().upper())) # thePlayer will be an empty string is invalid input is received


    print('Nice choice!')
    print('Here are the possible moves you can make:')
    print('\n')
    printKey(theBoard)
    print('\n')

    while isFull(theBoard) == False:

        print('Please enter your move.')
        makePlayerMove(input(), theBoard)


        if playerWon(theBoard):
            postGame('player', theBoard)

        elif isFull(theBoard):
            postGame('cat', theBoard)


        trivial_makeCPUMove(theBoard)
        #random_makeCPUMove(theBoard)


        if CPUWon(theBoard):
            postGame('cpu', theBoard)

        elif isFull(theBoard):
            postGame('cat', theBoard)

        print('\n')
        printBoard(theBoard)
        print('\n')






def playTest():
    b = {'top-L': 'O', 'top-M': 'X', 'top-R': 'O',  'mid-L': 'X', 'mid-M': 'X', 'mid-R': 'O', 'low-L': 'X', 'low-M': ' ', 'low-R': ' '}
    print('Let\'s play tic-tac-toe!')
    printBoard(b)
    print('Type X or O to play')
    assignLetter(str(input().upper())) # thePlayer will be an empty string is invalid input is received


    print('Nice choice!')
    print('Here are the possible moves you can make:')
    pprint.pprint(list(b.keys()))

    while isFull(b) == False:

        print('Please enter your move.')
        makePlayerMove(input(), b)

        if playerWon(b):
            printBoard(b)
            print('You won!')
            exit()

        elif isFull(b):
            printBoard(b)
            print('Aw, cat\'s game! Better luck next time!')
            exit()

        trivial_makeCPUMove(b)
        #random_makeCPUMove(theBoard)

        if CPUWon(b):
            printBoard(b)
            print('I win!')
            exit()

        elif isFull(b):
            printBoard(b)
            print('Aw, cat\'s game! Better luck next time!')
            exit()

        printBoard(b)
        print('\n')



#playTest()

playGame()
