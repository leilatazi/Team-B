#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:55:03 2018

@author: Javier
"""
#
#. Rock paper scissors: Implement a function that checks who from
#two players won a rock paper scissors game. The function should take
#two parameters, the first for what player 1 used, the second for what
#player 2 used, and return who won the match, either player 1 or player
#two.
#Create tests for this function too!
#

#%%

def game(p1,p2):
    
    if p1 == p2:
        return "Tie"
    if p1 == "Rock":
        if p2 == "Scissors":
            return "P1 won"
        else:
            return "P2 won"
    if p1 == "Scissors":
        if p2 == "Paper":
            return "P1 won"
        else:
            return "P2 won"
    if p1 == "Paper":
        if p2 == "Rock":
            return "P1 won"
        else:
            return "P2 won"
        
#game("Rock", "Paper")
#game("Rock", "Rock")
#game("Paper", "Rock")
#game("Paper", "Scissors")

#%%
#
#Modify your previous function so it works with rock-paper-scissorslizzard-spock.
#Modify your tests accordingly.

def second_game(p1,p2):
    
    valid_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    if p1 not in valid_options or p2 not in valid_options:
        return "Invalid input"
    
    if p1 == p2:
        return "Tie"
    if p1 == "Rock":
        if p2 == "Scissors" or p2 == "Lizard":
            return "P1 won"
        else:
            return "P2 won"
    if p1 == "Scissors":
        if p2 == "Paper" or p2 == "Lizard":
            return "P1 won"
        else:
            return "P2 won"
    if p1 == "Paper":
        if p2 == "Rock" or p2 == "Spock":
            return "P1 won"
        else:
            return "P2 won"
    if p1 == "Lizard":
        if p2 == "Spock" or p2 == "Paper":
            return "P1 won"
    if p1 == "Spock":
        if p2 == "Rock" or p2 == "Scissors":
            return "P1 won"
        else: 
            return "P2 won"

#second_game("Spock", "Lizard")
#second_game("Paper", "Lizard")
#second_game("P", "Lizard")

#%%

