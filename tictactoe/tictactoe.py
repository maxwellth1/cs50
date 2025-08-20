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

    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    return X if xCount == oCount else O


def actions(board):

    moves = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves

def result(board, action):

    copyBoard = copy.deepcopy(board)
    i,j = action
    currentPlayer = player(board)

    if copyBoard[i][j] is not EMPTY: 
        raise Exception("Invalid move")
    
    copyBoard[i][j] =  currentPlayer
    
    return copyBoard


def winner(board):

    #rows
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return X
        if row[0] == row[1] == row[2] == O:
            return O
     
    #columns
    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] == X):
            return X
        if(board[0][col] == board[1][col] == board[2][col] == O):
           return O
         
    #Diagonals
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O    

    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None


def terminal(board):
    
    if winner(board) is not None:
        return True
    
    elif sum(row.count(X) + row.count(O) for row in board) == 9:
        return True 
    
    else:
        return False 
    

def utility(board):
    
    if winner(board) == X:
     return 1
    
    elif winner(board) == O:
        return -1
    
    else:
        return 0


def maxValue(board, alpha, beta):
    
    if terminal(board):

        return utility(board)

    v = float('-inf')

    for action in actions(board):

        v = max(v,minValue(result(board,action), alpha, beta))
        alpha = max(alpha, v)

        if beta <= alpha:

            break

    return v


def minValue(board, alpha, beta):
    
    if terminal(board):

        return utility(board)

    v = float('inf')

    for action in actions(board):

        v = min(v,maxValue(result(board,action), alpha, beta))
        beta = min(beta, v)

        if beta <= alpha:

            break

    return v


def minimax(board):
    
    if terminal(board):

        return None
    
    currentPlayer = player(board)

    if currentPlayer == X:          #if X turn

        bestScore = float('-inf')
        bestMove = None

        for action in actions(board):

            score = minValue(result(board,action), float('-inf'), float('inf'))

            if score>bestScore:

                bestScore = score
                bestMove = action
        
        return bestMove
    
    else:                            #if O turn

        bestScore = float('inf')
        bestMove = None

        for action in actions(board):

            score = maxValue(result(board,action), float('-inf'), float('inf'))

            if score<bestScore:

                bestScore = score
                bestMove = action
        
        return bestMove
            


