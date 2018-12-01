# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:16:27 2018

@author: Leila
"""

from string_calculator import string_calculator

def test_string_calculator_returns19():
    assert string_calculator("2,3,4,5,3,2") == 19
    
def test_string_calculator_returnsNone():
    assert string_calculator("") == 0
    
    