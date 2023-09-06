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
    if action in actions(board):
        resultboard[action[0]][action[1]] = player(board)
    else:
        raise Exception("Action is not possible")

    return resultboard
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns = [[],[],[]]
    winner = None
    
    diagonalLR = []
    diagonalLR.append(board[0][0])
    diagonalLR.append(board[1][1])
    diagonalLR.append(board[2][2])
    if diagonalLR.count(diagonalLR[0]) == 3 and diagonalLR[0] != EMPTY:
        winner = diagonalLR[0]

    diagonalRL = []
    diagonalRL.append(board[0][2])
    diagonalRL.append(board[1][1])
    diagonalRL.append(board[2][0])

    if diagonalRL.count(diagonalRL[0]) == 3 and diagonalRL[0] != EMPTY:
        winner = diagonalRL[0]

    for row in board:
        if (row.count(row[0]) == 3) and row[0] != EMPTY:
            winner = row[0] 
    for row in board:
        columns[0].append(row[0])
        columns[1].append(row[1])
        columns[2].append(row[2])
    
    for column in columns:
        if (column.count(column[0]) == 3) and column[0] != EMPTY:
            winner = column[0] 
    

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    full = []
    finished = False
    for row in board:
        for item in row:
            full.append(item)
    
    if (full.count(EMPTY)) == 0:
         finished = True
    
    if winner(board) != None:
        finished= True
    
    return finished


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility = 0
    if terminal(board) == True:
        if winner(board) == X:
            utility = 1
        if winner(board) == O:
            utility = -1

    return utility


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    boards = [board]
    
    full = []
    finished = False
    for row in board:
        for item in row:
            full.append(item)
    
    movesleft=full.count(EMPTY)
    for action in actions(board):
        print (action)
        print(result(board, action))


    
    


board = initial_state()
minimax(board)