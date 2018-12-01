# -*- coding: utf-8 -*-

#Tictactoe: Create tests for your implementation of the tictactoe board
#checker functions.

#%%
from tictactoe import solved_horizontal

def test_horizontal_lost():
    values = [[
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']
    ],
    [
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']]
    ]
    for case in values:
        assert solved_horizontal(case) == "You lost!"
    
def test_horizontal_won():
    values = [[
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'x', 'x']
    ],
    [
    ['x', 'x', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']]
    ]
    for case in values:
        assert solved_horizontal(case) == "You won!"
        
        
#%%

from tictactoe import solved_vertical

def test_vertical_lost():
    values = [[
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']
    ],
    [
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']]
    ]
    for case in values:
        assert solved_vertical(case) == "You lost!"
    
def test_vertical_won():
    values = [[
    ['x', 'o', 'x'],
    ['x', 'x', 'o'],
    ['x', 'x', 'x']
    ],
    [
    ['x', 'x', 'x'],
    ['o', 'x', 'x'],
    ['x', 'o', 'x']]
    ]
    for case in values:
        assert solved_vertical(case) == "You won!"


        
#%%

from tictactoe import solved_diagonal

def test_diagonal_lost():    
    values = [[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'o',"o"],
    ['x', 'x', 'x',"x"],
    ['x', 'o', 'x',"x"]
    ],
    [['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"o"],
    ['x', 'o', 'x',"x"],
    ['x', 'o', 'x',"x"]]
    ]
    
    for case in values:
        assert solved_diagonal(case) == "You lost!"

def test_diagonal_won():    
    values = [[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"o"],
    ['x', 'x', 'x',"x"],
    ['x', 'o', 'x',"x"]
    ],
    [['x', 'x', 'o',"x"],
    ['o', 'x', 'x',"o"],
    ['x', 'o', 'x',"x"],
    ['x', 'o', 'x',"x"]]
    ]
    
    for case in values:
        assert solved_diagonal(case) == "You won!"

#%%
        
from tictactoe import solved_tic_tac_toe

def test_solved_tictactoe_lost():
    
    values = [[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"x"],
    ['x', 'o', 'x',"o"],
    ['x', 'x', 'o',"x"]
    ],[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"x"],
    ['x', 'o', 'x',"o"],
    ['x', 'x', 'o',"x"]
    ]
    ]
        
    for case in values:
        assert solved_tic_tac_toe(case) == "You lost!"
        
def test_solved_tictactoe_won():
    
    values = [[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"x"],
    ['x', 'o', 'x',"x"],
    ['x', 'x', 'o',"x"]
    ],[
    ['x', 'x', 'o',"x"],
    ['o', 'o', 'x',"x"],
    ['x', 'x', 'x',"o"],
    ['x', 'x', 'o',"x"]
    ]
    ]
        
    for case in values:
        assert solved_tic_tac_toe(case) == "You won!"