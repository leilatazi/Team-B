#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:26:03 2018

@author: Javier
"""
#%%

from rock_paper_scissors import game
from rock_paper_scissors import second_game


def test_rock_paper_scissors_invalid_input():
    mylist = []
    
    for case in mylist:
        assert game(mylist) == "Invalid input"
        
def test_rock_paper_scissors_rock_wins():
    assert game("Paper", "Rock") == "P1 won"
    
def test_rock_paper_scissors_scissors_wins():
    assert game("Paper", "Scissors") == "P2 won"
    
def test_rock_paper_scissors_tie():
    assert game("Paper", "Paper") == "Tie"
    
def test_rock_paper_scissors_lizard_spock_invalid_input():
    mylist = []
    
    for case in mylist:
        assert second_game(mylist) == "Invalid input"

def test_rock_paper_scissors_lizard_wins():
    assert second_game("Lizard", "Paper") == "P1 won"

def test_rock_paper_scissors_spock_wins():
    assert second_game("Rock", "Spock") == "P2 won"
    