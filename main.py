import random

def board():
    return [["" for _ in range (3)] for _ in range (3)]

def print_board(board):
    print('\n')
    for i, r in enumerate(board):
        print(' | '.join(r))
        if i < 2:
            print('---------')
    print('\n')

def moves(board):
    return any("" in r for r in board) 

def win(board):
    for r in board:
        if r[0] == r[1] == r[2] and r[0] != "":
            return r[0]
        
    #comment 