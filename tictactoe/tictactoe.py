"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nbrOfX = 0
    nbrOfO = 0
    for row in board:
        for cell in row:
            if cell == X:
                nbrOfX += 1
            elif cell == 0:
                nbrOfO += 1
    if nbrOfX > nbrOfO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for row in range(board):
        for cell in range(row):
            if board[row][cell] == EMPTY:
                actionSet.add((row, cell))
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise RuntimeError('Trying to make a move on a non-empty cell')
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    threeInARow = []
    for row in range(board):
        for col in range(row):
            threeInARow.append(board[row][col])
        if is_three_in_a_row(threeInARow):
            return threeInARow[0]

    threeInARow = []
    for col in range(board):
        for row in range(col):
            threeInARow.append(board[row][col])
        if is_three_in_a_row(threeInARow):
            return threeInARow[0]

    firstDiagonal = [board[0][0], board[1][1], board[2][2]]
    if is_three_in_a_row(firstDiagonal):
        return firstDiagonal[0]
    secondDiagonal = [board[0][2], board[1][1], board[2][0]]
    if is_three_in_a_row(secondDiagonal):
        return secondDiagonal[0]

    return None


def is_three_in_a_row(row):
    if len(row) == 3:
        if row[0] == row[1] and row[0] == row[2] and row[0] != EMPTY:
            return True
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in range(board):
        for cell in range(row):
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    goldMedalist = winner(board)

    if goldMedalist == X:
        return 1
    elif goldMedalist == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
