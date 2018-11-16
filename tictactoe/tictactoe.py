#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:48:24 2018

@author: Javier
"""

#%%

board = [
['x', 'x', 'x'],
['o', 'x', 'o'],
['x', 'o', 'x']
]


def solved_horizontal(board):
    
    for row in board:
        if row.count("x") == len(row):
            return "You won!"  
    return "You lost!"

solved_horizontal(board)


#%%
    
board = [
['x', 'x', 'o',"x"],
['o', 'o', 'o',"x"],
['x', 'x', 'x',"x"],
['x', 'x', 'x',"x"]
]

    
def solved_vertical(board):
    
    solved = "You lost!"
    length = len(board)
    count_x = 0
    
    for c in range(length):
        count_x = 0
        for r in range(length):
            if board[r][c] == "x":
                count_x += 1
                if count_x == length :
                    solved = "You won!"
    return solved
    

                    
solved_vertical(board)

#%%

board = [
['x', 'x', 'o',"x"],
['o', 'o', 'x',"o"],
['x', 'x', 'x',"x"],
['x', 'o', 'x',"x"]
]

    
def solved_diagonal(board):
    
    solved = "You lost!"
    length = len(board)
    count_x = 0

    
    for i in range(length):
        if board[i][i] == "x":
            count_x += 1
      
            if count_x == length :
               solved = "You won!"
    
    c = length -1 
    count_x = 0
    
    for r in range(length):
        if board[r][c] == "x":
            count_x += 1
            c -= 1
            if count_x == length :
                solved = "You won!"    
                    
    
    return solved
    
solved_diagonal(board)

#%%
board = [
['x', 'x', 'o',"x"],
['o', 'x', 'x',"x"],
['x', 'o', 'x',"o"],
['x', 'x', 'o',"x"]
]

def solved_tic_tac_toe(board):
    if solved_horizontal(board) == "You won!":
        return "You won!"
    elif solved_vertical(board) == "You won!":
        return "You won!"
    elif solved_diagonal(board) == "You won!":
        return "You won!"
    else:
        return "You lost!"
    
solved_tic_tac_toe(board)

#%%
