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
            elif cell == O:
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
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                actionSet.add((i, j))
            j += 1
        i += 1
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise RuntimeError('No action')
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
    for i in range(3):
        for j in range(3):
            threeInARow.append(board[i][j])
        if is_three_in_a_row(threeInARow):
            return threeInARow[0]
        threeInARow.clear()

    threeInARow = []
    for i in range(3):
        for j in range(3):
            threeInARow.append(board[j][i])
        if is_three_in_a_row(threeInARow):
            return threeInARow[0]
        threeInARow.clear()

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

    for row in board:
        for cell in row:
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
    if X -> max, if O -> min
    """
    best = BestAction
    if player(board) == X:
        best = maximum(board)
    elif player(board) == O:
        best = minimum(board)

    return best.action


def minimum(board):
    best = BestAction(None, 2)

    if terminal(board):
        best.action = None
        best.value = utility(board)
        return best

    for action in actions(board):
        v = maximum(result(board, action)).value
        if v < best.value:
            best.action = action
            best.value = v

    return best


def maximum(board):
    best = BestAction(None, -2)

    if terminal(board):
        best.action = None
        best.value = utility(board)
        return best

    for action in actions(board):
        v = minimum(result(board, action)).value
        if v > best.value:
            best.action = action
            best.value = v

    return best

class BestAction:
    def __init__(self, action, value):
        self.action = action
        self.value = value
