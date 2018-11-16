# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:56:09 2018

@author: Leila
"""

#%%

from tictactoe import *

def test_vertical_won():
    
    case = [
['x', 'x', 'o',"x"],
['x', 'x', 'x',"x"],
['x', 'o', 'x',"o"],
['x', 'x', 'o',"x"]
]
    
    assert solved_vertical(case) == "You won!"
    
def test_vertical_lost():
        
    case = [
['x', 'x', 'o',"x"],
['o', 'x', 'x',"x"],
['x', 'o', 'o',"o"],
['x', 'x', 'o',"x"]
]
    
    assert solved_vertical(case) == "You lost!"
    
def test_diagonal_won():
    
    case1 = [
['x', 'x', 'o',"x"],
['x', 'x', 'x',"x"],
['o', 'o', 'x',"o"],
['x', 'x', 'o',"x"]
]
     case2 = [
['x', 'x', 'o',"x"],
['x', 'o', 'x',"x"],
['o', 'x', 'x',"o"],
['x', 'x', 'o',"x"]
]
    
    assert solved_diagonal(case1) == "You won!"
    assert solved_diagonal(case2) == "You won!"