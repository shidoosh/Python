import pprint
import random



theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
letters = ['X', 'O']
difficulties = ['easy', 'intermediate', 'hard']
CPUMoveCount = 0


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

def assignDifficulty(difficulty):
    while difficulty not in difficulties:
        print('Only easy, intermediate, or hard is allowed. Please try again.')
        difficulty = str(input().lower())

    return difficulty


def isFull(board):
    # check if cat's game
    if ' ' in board.values():
        return False
    else:
        return True

def twoInRow(letter, board):
    # rows
    # top row
    if board['top-L'] == letter and board['top-L'] == board['top-M']: # x \ x \ _
        if board['top-R'] == ' ':
            return 'top-R'
    if board['top-M'] == letter and board['top-M'] == board['top-R']: # _\ x \ x
        if board['top-L'] == ' ':
            return 'top-L'
    if board['top-L'] == letter and board['top-L'] == board['top-R']: # x \ _ \ x
        if board['top-M'] == ' ':
            return 'top-M'

    # middle row

    if board['mid-L'] == letter and board['mid-L'] == board['mid-M']: # x \ x \ _
        if board['mid-R'] == ' ':
            return 'mid-R'
    if board['mid-M'] == letter and board['mid-M'] == board['mid-R']: # _\ x \ x
        if board['mid-L'] == ' ':
            return 'mid-L'
    if board['mid-L'] == letter and board['mid-L'] == board['mid-R']: # x \ _ \ x
        if board['mid-M'] == ' ':
            return 'mid-M'
    # bottom row

    if board['low-L'] == letter and board['low-L'] == board['low-M']: # x \ x \ _
        if board['low-R'] == ' ':
            return 'low-R'
    if board['low-M'] == letter and board['low-M'] == board['low-R']: # _\ x \ x
        if board['low-L'] == ' ':
            return 'low-L'
    if board['low-L'] == letter and board['low-L'] == board['low-R']: # x \ _ \ x
        if board['low-M'] == ' ':
            return 'low-M'


    # columns
    # left column
    if board['top-L'] == letter and board['top-L'] == board['mid-L']:
        if board['low-L'] == ' ':
            return 'low-L'

    if board['mid-L'] == letter and board['mid-L'] == board['low-L']:
        if board['top-L'] == ' ':
            return 'top-L'

    if board['top-L'] == letter and board['top-L'] == board['low-L']:
        if board['mid-L'] == ' ':
            return 'mid-L'

    # mid column
    if board['top-M'] == letter and board['top-M'] == board['mid-M']:
        if board['low-M'] == ' ':
            return 'low-M'

    if board['mid-M'] == letter and board['mid-M'] == board['low-M']:
        if board['top-M'] == ' ':
            return 'top-M'

    if board['top-M'] == letter and board['top-M'] == board['low-M']:
        if board['mid-M'] == ' ':
            return 'mid-M'

    # right column
    if board['top-R'] == letter and board['top-R'] == board['mid-R']:
        if board['low-R'] == ' ':
            return 'low-R'

    if board['mid-R'] == letter and board['mid-R'] == board['low-R']:
        if board['top-R'] == ' ':
            return 'top-R'

    if board['top-R'] == letter and board['top-R'] == board['low-R']:
        if board['mid-R'] == ' ':
            return 'mid-R'

    # diagonals
    # negative diagonal
    if board['top-L'] == letter and board['top-L'] == board['mid-M']:
        if board['low-R'] == ' ':
            return 'low-R'

    if board['top-L'] == letter and board['top-L'] == board['low-R']:
        if board['mid-M'] == ' ':
            return 'mid-M'

    if board['mid-M'] == letter and board['mid-M'] == board['low-R']:
        if board['top-L'] == ' ':
            return 'top-L'

    # positive diagonal
    if board['low-L'] == letter and board['low-L'] == board['mid-M']:
        if board['top-R'] == ' ':
            return 'top-R'
    if board['low-L'] == letter and board['low-L'] == board['top-R']:
        if board['mid-M'] == ' ':
            return 'mid-M'
    if board['mid-M'] == letter and board['mid-M'] == board['top-R']:
        if board['low-L'] == ' ':
            return 'low-L'

    return None

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

def setupCPU(board):
    randomChoice = random.choice(list(board.items()))
    for m, l in board.items():
        if l == theCPU:
            match m:
                case 'top-L':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'mid-R' or randomChoice[0] == 'low-M':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'top-M':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'mid-L' or randomChoice[0] == 'mid-R' or randomChoice[0] == 'low-L' or randomChoice[0] == 'low-R':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'top-R':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'mid-L' or randomChoice[0] == 'low-M':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice

                case 'mid-L':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'top-M' or randomChoice[0] == 'top-R' or randomChoice[0] == 'low-M' or randomChoice[0] == 'low-R':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'mid-M':
                    while randomChoice[1] != ' ': # choice needs to be empty spot on the board, any spot is okay
                        randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'mid-R':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'top-L' or randomChoice[0] == 'top-M' or randomChoice[0] == 'low-L' or randomChoice[0] == 'low-M':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'low-L':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'top-M' or randomChoice[0] == 'mid-R':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice

                case 'low-M':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'top-L' or randomChoice[0] == 'top-R' or randomChoice[0] == 'mid-L' or randomChoice[0] == 'mid-R':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

                case 'low-R':
                    while randomChoice[1] != ' ' or randomChoice[0] == 'top-M' or randomChoice[0] == 'mid-L':
                            randomChoice = random.choice(list(board.items()))
                    return randomChoice[0]

        # CPU hasn't made a move
        else:
            if board['mid-M'] == ' ':
                return 'mid-M'
            else:
                while randomChoice[1] != ' ': # choice needs to be empty spot on the board
                    randomChoice = random.choice(list(board.items()))
                return randomChoice[0]

# not in use, just for practice
def offense_makeCPUMove(board):
    #row
    if board['top-L'] == theCPU and board['top-L'] == board['top-M']:
        if(board['top-R'] == ' '):
            board['top-R'] = theCPU
            return

    if board['mid-L'] == theCPU and board['mid-L'] == board['mid-M']:
        if(board['mid-R'] == ' '):
            board['mid-R'] = theCPU
            return

    if board['low-L'] == theCPU and board['low-L'] == board['low-M']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return


    #column
    if board['top-L'] == theCPU and board['top-L'] == board['mid-L']:
        if(board['low-L'] == ' '):
            board['low-L'] = theCPU
            return

    if board['top-M'] == theCPU and board['top-M'] == board['mid-M']:
        if(board['low-M'] == ' '):
            board['low-M'] = theCPU
            return

    if board['top-R'] == theCPU and board['top-R'] == board['mid-R']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return


    #diagonal
    if board['top-L'] == theCPU and board['top-L'] == board['mid-M']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return

    if board['low-L'] == theCPU and board['low-L'] == board['mid-M']:
        if(board['top-R'] == ' '):
            board['top-R'] = theCPU
            return

    random_makeCPUMove(board)

# not in use, just for practice
def defense_makeCPUMove(board):
    #row
    if board['top-L'] == thePlayer and board['top-L'] == board['top-M']:
        if(board['top-R'] == ' '):
            board['top-R'] = theCPU
            return


    if board['mid-L'] == thePlayer and board['mid-L'] == board['mid-M']:
        if(board['mid-R'] == ' '):
            board['mid-R'] = theCPU
            return

    if board['low-L'] == thePlayer and board['low-L'] == board['low-M']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return


    #column
    if board['top-L'] == thePlayer and board['top-L'] == board['mid-L']:
        if(board['low-L'] == ' '):
            board['low-L'] = theCPU
            return

    if board['top-M'] == thePlayer and board['top-M'] == board['mid-M']:
        if(board['low-M'] == ' '):
            board['low-M'] = theCPU
            return

    if board['top-R'] == thePlayer and board['top-R'] == board['mid-R']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return


    #diagonal
    if board['top-L'] == thePlayer and board['top-L'] == board['mid-M']:
        if(board['low-R'] == ' '):
            board['low-R'] = theCPU
            return

    if board['low-L'] == thePlayer and board['low-L'] == board['mid-M']:
        if(board['top-R'] == ' '):
            board['top-R'] = theCPU
            return

    offense_makeCPUMove(board)



# make smart
def smart_CPUMove(board):

    CPUmove = twoInRow(theCPU, board)
    PlayerMove = twoInRow(thePlayer, board)
    if CPUmove == None: # no winning moves for CPU
        if PlayerMove == None: # check if need to defend
            board[setupCPU(board)] = theCPU # CPU free to set up a play since no need to defend
        else: # need to defend
            board[PlayerMove] = theCPU
    else: # make winning move for CPU
        board[CPUmove] = theCPU






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
    print('Please select a difficulty: easy, intermediate, hard')
    difficulty = assignDifficulty(str(input().lower()))
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



        if(difficulty == 'easy'):
            trivial_makeCPUMove(theBoard)
        if(difficulty == 'intermediate'):
            random_makeCPUMove(theBoard)
        if(difficulty == 'hard'):
            #defense_makeCPUMove(theBoard)
            smart_CPUMove(theBoard)


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
