# -*- coding: utf-8 -*-
"""
Assignment 1 Magic Trick
01/12/2025
"""

from datetime import datetime
try:
        current_year = datetime.now().year
        number = int(input("Pick a number between 1 and 9: "))
        
        result = number * 2
        
        result += 5
        
        result *= 50
        
        result += current_year - 253
        
        result += 2
        
        result -= 2002
    
        print(f"Result is: {result}")
    
        orginal_number = result // 100
        age = result % 100
        
        print(f"The orignal number is {orginal_number}")
        print(f"Your age is {age}")
    
except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")







