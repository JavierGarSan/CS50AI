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
    return [[X, EMPTY, O],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, X]]


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
    resultboard = copy.deepcopy(board)
    actionsPosible =actions(resultboard)
    if action in actionsPosible:
        resultboard[action[0]][action[1]] = player(resultboard)
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
    if winner(board) == X:
        utility = 1
    if winner(board) == O:
        utility = -1

    return utility


def evaluation(board, actions):
    eva=[]
    for possible in actions:
        if terminal(result(board, possible)):
            eva.append(utility(result(board, possible)))
            print()

    return eva
# Define the function that removes a node from the frontier and returns it.


def remove(self):
        # Terminate the search if the frontier is empty, because this means that there is no solution.
    if len(self) == 0:
        raise Exception("empty frontier")
    else:
            # Save the last item in the list (which is the newest node added)
        node = self[-1]
        # Save all the items on the list besides the last node (i.e. removing the last node)
        self = self[:-1]
        return node

def add(board, self):
    for action in actions(board):
        self.append(action)
    
    return self

def MaxorMin(board):
    if player(board) ==X:
        return "Max"
    if player(board) == O:
        return "Min"

def maximising(board,optimal):
    v=-math.inf
    results = []
    if terminal(board):
       return(utility(board))
    for action in actions(board):
        if terminal(result(board,action)):
            if utility(result(board,action)) == 1:
                optimal = action
            results.append(utility(result(board,action)))

    
    v = max(v,min(results))
        
    return v, optimal

def minimising(board):
    v=math.inf()
    
        

def minimax(board,optimal):
    if maximising(board,optimal)[0] == 1:
        print("1 found")
        optimal = maximising(board,optimal)[1]


    return optimal
            
optimal=""
self = []
oBoard = initial_state()
self = add(oBoard, self)
action = (remove(self))
print(action)