# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:15:56 2018

@author: Leila
"""

#
#4. String calculator: Create a function string_calculator that takes
#a string as parameter and sums the digitw it contains. In the input
#string, the numbers should be separated by a comma. Trying to sum
#an empty string should return zero.
#Input examples:
#
#""
#"4"
#"2,3,4,5,3,2"
#Create tests for this function.

#%%

def string_calculator(string):
    
    first_list = string
    second_list = []
    third_list = []
    
    for i in first_list:
        second_list.append(i)

    print(second_list)
    for i in second_list:
        if i != ",":
            third_list.append(i)
            
    print(third_list)
    
    list_of_integers = [int(x) for x in third_list]
    
    print(list_of_integers)
    return sum(list_of_integers)
        

string_calculator("")
