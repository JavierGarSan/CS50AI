"""
Tic Tac Toe Player
"""

import math

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
    xTotal = 0
    oTotal = 0
    for row in board:
        for item in row:
            if item == X:
                xTotal += 1
            if item == O:
                oTotal += 1

    if xTotal > oTotal:
        return(O)

    if xTotal == oTotal:
        return(X)
    """
    Returns player who has the next turn on a board.
    """

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible.add((i,j))

    return(possible)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultboard = board
    if action in possible:
        resultboard[action[0]][action[1]] = currentPlayer
    else:
        raise Exception("Action is not possible")

    return resultboard
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


board = initial_state()
currentPlayer = player(board)
possible = actions(board)
print(result(board, (0,0)))
