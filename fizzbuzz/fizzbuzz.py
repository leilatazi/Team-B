# -*- coding: utf-8 -*-
#5. Fizzbuzzwhiz: Modify our Fizzbuzz implementation to add a new
#case Whiz. the fizzbuzzwhiz function should return Whiz when the
#given number is prime.
#Write tests for it too

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
