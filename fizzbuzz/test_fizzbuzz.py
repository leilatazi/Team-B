#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:29:58 2018

@author: efrancois
"""
#%%
from fizzbuzz import fizzbuzzwhiz

def test_fizzbuzz_returns_fizz():
    assert fizzbuzzwhiz(3) == "Fizz"
    assert fizzbuzzwhiz(6) == "Fizz"
    assert fizzbuzzwhiz(12342) == "Fizz"
    
def test_fizzbuzz_returns_buzz():
    values = [10,100, 1000,]
    
    for case in values:
        assert fizzbuzzwhiz(case) == "Buzz"
        
def test_fizzbuzz_returns_fizzbuzz():
    values = [15,30,45, 90]
    
    for case in values:
        assert fizzbuzzwhiz(case) == "FizzBuzz"


def test_fizzbuzz_returns_whiz():
    values = [2,7,11,17,23,29,31]
    
    for case in values:
        assert fizzbuzzwhiz(case) == "Whiz"

