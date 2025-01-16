# -*- coding: utf-8 -*-
"""
Assignment 1 Magic Trick
01/12/2025
"""


try:
        number = int(input("Pick a number between 1 and 9: "))
        
        result = number * 2
        
        result += 5
        
        result *= 50
        
        result += 1749
        
        result += 25
        
        result -= 2002
    
        print(f"Result is: {result}")
    
        orginal_number = result // 100
        #The orginal
        age = result % 100
        
        print(f"The orignal number is {orginal_number}")
        print(f"Your age is {age}")
    
except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")


# Since you added the input function, you should have also considered adding
# inputs for parts e and f so that the function can work any time, any year. 




