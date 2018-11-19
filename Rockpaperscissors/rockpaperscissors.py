# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:34:48 2018

@author: Leila
"""

#%%

p1 = "paper"
p2 = "paper"

def rockpaperscissors(p1,p2):
    game = [p1,p2]
    if game == ["rock","paper"] or game == ["paper","scissors"] or game == ["scissors","rock"]:
        print ("Player 2 wins!")
    elif game == ["paper","rock"] or game == ["scissors","paper"] or game == ["rock","scissors"]:
        print ("Player 1 wins!")
    elif p1 == p2:
        print ("Tie")

rockpaperscissors(p1,p2)