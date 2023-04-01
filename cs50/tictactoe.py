"""
Tic Tac Toe Player
"""

import math, random, copy

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
    board_str = str(board)
    #print(type(board))
    #print(type(board_str))
    #print(board_str.count("None"), board_str.count("X"), board_str.count("O"))
    
    if board_str.count("None") == 9: # initial game state, player X has the first move
        next_player = X
    elif board_str.count("None") == 0: # end of the game
        next_player = "game finished"
    elif board_str.count("X") > board_str.count("O"): # player O is next
        next_player = O
    elif board_str.count("X") <= board_str.count("O"): # player X is next
        next_player = X
    else: print("could not decide who is next")
    return next_player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None: set.append((i, j))
    return set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != None:
        raise Exception("action is not a valid for the board")
    else:
        """
        new_board_state = []
        for i in range(len(board)):
            row = []
            for j in range(len(board[i])):
                row.append(board[i][j])
            new_board_state.append(row)
        """
        new_board_state = copy.deepcopy(board)
        new_board_state[action[0]][action[1]] = player(board)
        return new_board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def check_triple(player):
        condition = False
        for i in range(len(board)): # check triple horizontally
            if str(board[i]).count(player) == 3: condition = True
        for i in range(3): # check vertically
            for j in range(3):
                col = []
                col.append((board[0][i], board[1][i], board[2][i]))
                # print(str(col).count(player))
                if str(col).count(player) == 3: condition = True
            # print(board[i])
            # print(board[0][i] == player, board[1][i] == player, board[2][i] == player)
            # if board[0][i] == player and board[1][i] == player and board[2][i] == player: condition == True
        # check both diagonal options
        # print(str((board[0][0],board[1][1],board[2][2])).count(player), str((board[0][0],board[1][1],board[2][2])).count(player) ==3)
        if str((board[0][0],board[1][1],board[2][2])).count(player) == 3: condition = True
        if str((board[0][2],board[1][1],board[2][0])).count(player) == 3: condition = True
        return condition
    
    # print(board)
    if check_triple("X") == True: return "X"
    elif check_triple("O") == True: return "O"
    else: return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    board_str = str(board)
    if board_str.count("None") == 0 or winner(board) != None: # end of the game
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        print(board, winner(board))
        if winner(board) == "X": return 1
        if winner(board) == "O": return -1
        if winner(board) == None: return 0
    elif terminal(board) == False: return 0
    else: raise Exception("utility can not be estimated")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True: return None
    else: 
        poss_moves = actions(board)
        next_move = poss_moves[random.randint(0,len(poss_moves)-1)]
        print(poss_moves, len(poss_moves), next_move)
        next_player = player(board)
        # print("next player", next_player)
        utilities = []
        for i in range(2):
            if i == 0: next_player = "O"
            if i == 1: next_player = "X"
            for i in range(len(poss_moves)):
                poss_board = copy.deepcopy(board)
                poss_board[poss_moves[i][0]][poss_moves[i][1]] = next_player
                print(poss_board)
                utilities.append(utility(poss_board))
            print(utilities)
        poss_moves = poss_moves * 2
        if utilities.count(0) != len(utilities): # recognize possbility of win/loose
            if player(board) == "X":
                if utilities.count(1) > 0:
                    next_move = poss_moves[utilities.index(1)] # player X goes for win
                else: 
                    next_move = poss_moves[utilities.index(-1)] # if there is no chance to win for player X, then avoid loose
            if player(board) == "O":
                if utilities.count(-1) > 0:
                    next_move = poss_moves[utilities.index(-1)]
                else: 
                    next_move = poss_moves[utilities.index(1)]            
        return next_move