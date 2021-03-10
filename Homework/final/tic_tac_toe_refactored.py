# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

def drawBoard(board):
    """ This function prints out the board that it was passed.
    Inputs: 
        board - is a list of 10 strings representing the board (ignore index 0). 
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    """ Lets the player type which letter they want to be.
    Returns: 
        A list with the player’s letter as the first item, and the computer's letter as the second. 
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def whoGoesFirst():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def playAgain():
    """ This function determins whether player wants to replay.
    Returns:
        True if players wants to play again.
        False if player doesn't want to play again.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """ Given a board and a player’s letter, this function returns True if that player has won. We use bo instead of board and le instead of letter so we don’t have to type as much.
    Inputs:
        bo - the board
        le - letter

    Returns:
        True if there's a wining combination.
        False if there's not a wining combination.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    """ Make a duplicate of the board list and return it the duplicate.
    Inputs:
        board - the board

    Returns:
        A copy of the board.
    """

    return board.copy()

def isSpaceFree(board, move):
    """ Checks if there's space to add X or O
    Inputs:
        board - the board
        move - the integer corresponding to the board

    Return:
        True if the passed move is free on the passed board.
    """
    return board[move] == ' '

def getPlayerMove(board):
    """ Let the player type in their move.

    Returns:
        The integer of which the player chooses or types in.
    """
    inputMove = ' ' 
    while inputMove not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(inputMove)):
        print('What is your next move? (1-9)')
        inputMove = input()
    return int(inputMove)

def chooseRandomMoveFromList(board, movesList):
    """ Chooses a random move from a list.
    Returns:
        A valid move from the passed list on the passed board.
        Or None if there is no valid move.
    """
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves:
        return random.choice(possibleMoves)
    # TODO: is this 'else' necessary? - done
    return None

def getComputerMove(board, computerAssignedLetter):
    """ Given a board and the computer's letter, determine where to move and return that move. 
    Inputs:
        board - the board
        computerAssignedLetter - the letter that's assgined to the computer

    Returns:
        The integer for the computer's move on the board
    """
    global playerLetter
    if computerAssignedLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerAssignedLetter, i)
            if isWinner(copy, computerAssignedLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    choosenMove = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if choosenMove is not None:
        return choosenMove

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """ Checks if the board is full.
    Inputs:
        board - the board

    Returns: 
        True if every space on the board has been taken. 
        Otherwise return False.
    """
    for i in range(1, BOARD_SIZE):
        if isSpaceFree(board, i):
            return False
    return True

def isGameTied(board):
    """ Checks to see if game is tied.
    Inputs:
        board - the board

    Returns:
        True if game is tied.
        False if game is not tied.
    """
    if isBoardFull(board):
        drawBoard(board)
        print('The game is a tie!')
        return True
    return False

def isPlayerWinner(board, letter):
    """ Checks to see if the player won or there's a tie.
    Inputs:
        board - the board
        letter - player's letter

    Returns:
        True ig game is won by player or there's a tie.
        False if game is not yet won by player.
    """
    drawBoard(board)
    move = getPlayerMove(board)
    makeMove(board, letter, move)

    if isWinner(board, letter):
        drawBoard(theBoard)
        print('Hooray! You have won the game!')
        return True
    return False

def isComputerWinner(board, letter):
    """ Checks to see if the computer wins or there's a tie.
    Inputs:
        board - the board
        letter - computer's letter

    Returns:
        True ig game is won by computer or there's a tie.
        False if game is not yet won by computer.
    """
    move = getComputerMove(board, letter)
    makeMove(board, letter, move)

    if isWinner(board, letter):
        drawBoard(board)
        print('The computer has beaten you! You lose.')
        return True
    return False


print('Welcome to Tic Tac Toe!')

BOARD_SIZE = 10
while True:
    # Reset the board
    theBoard = [' '] * BOARD_SIZE 
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if isGameTied(theBoard):
            break
        if turn == 'player':
            if isPlayerWinner(theBoard, playerLetter):
                break
            turn = 'computer'
        else:
            # Computer’s turn.
            if isComputerWinner(theBoard, computerLetter):
                break
            turn = 'player'

    if not playAgain():
        break

