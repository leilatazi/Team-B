#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:21:46 2018

@author: Javier
"""
#
#Fizzbuzzwhiz: Modify our Fizzbuzz implementation to add a new
#case Whiz. the fizzbuzzwhiz function should return Whiz when the
#given number is prime.
#Write tests for it too.
#%%
def fizzbuzzwhizz(num):  
    
    counter = 0
   
    for i in range(2,num//2):
        if num % i == 0:
            counter += 1
    if counter <= 0 and num != 1:
        return "Whizz"    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"  
    else:
        return num
     
fizzbuzzwhizz(15)

#%%

def fizzbuzzwhiz(num):
    
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    
    if num % 3 == 0:
        return "Fizz"
    
    elif num % 5 == 0:
        return "Buzz"
    
    elif num > 1:
        for i in range(2,num):
            if num % i == 0:
                return num
                break
        else:
            return "Whiz"
        
    else:
        return num

fizzbuzzwhizz(15)
