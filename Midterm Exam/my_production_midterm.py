# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
def total_revenue(num_of_units_sold, fixed_price): # expected input/output? (-1)
    """Return the total revenue earned by a firm from selling products at a fixed_
    price multiply by the num_of_units_sold.

    total_revenue(450, 32)
    14400

    total_revenue(100, 20)
    2000

    total_revenue(50, 40)
    2000
   """
    # needs either a precondition or checks to make sure that variables are not negative (-1)

    revenue_earned = num_of_units_sold * fixed_price
    return revenue_earned

def total_cost(a, q, b): # expected input/output? (-1)
    """Return the total cost incurred by a firm to produce a product, where q
    is the quanity produces, b is the fixed cost, and a is the variable cost,
    which is a constant multiplied by the square of q.

    >>> total_cost(10, 10, 200)
    1200.0
    >> total_cost(12.5, 25, 350)
    8162.50
    >>> total_cost(23, 100, 1600)
    231600
    """
    # output would not include dollar signs. (-1)
    # needs either a precondition or checks to make sure that variables are not negative (-1)
    

    TC = (a * (q ** 2)) + b
    return TC



#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 2a
def total_profit(num_units: float, unit_price: float, multiplier:float, fixed_cost:float) ->float:
    """
        Calculate the total profit by taking total revenue (num_units * unit_price) minus 
        total cost (multiplier + fixed cost * num_units **2)
        
    >>>total_profit(15, 300, 10, 50)
    2200.0
    
    >>>total_profit(10, 300, 20, 50)
    950
    >>>total_profit(20, 500, 10, 50)
    5950.00
    """
    
    TR = num_units * unit_price
    TC = float((multiplier * (num_units ** 2) + fixed_cost))
    
    TP = TR - TC
    
    return TP

num_units = int(input("What is the quantity? "))
unit_price = float(input("What is unit price? "))
multiplier = int(input("What is multiplier? "))
fixed_cost = float(input("What the fixed price? "))

TR = total_profit(num_units, unit_price, multiplier, fixed_cost)
round_TR = round(total_profit(num_units, unit_price, multiplier, fixed_cost), 2)

print(f"The Total Profit is {round_TR}")

# Exercise 2b

def max_profit_calc(unit_price: float, multiplier: float, fixed_cost: float) -> float:
    """Calcuate the number of quantity produce to maximise profit.
        
    
    >>>max_profit_calc(100, .10, 2)
    500
    
    >>>max_profit_calc(500, .10, 5)
    1000
    >>>max_profit_calc(200, .02, 50)
    200
    """
    
    q_star = unit_price / (2 * mulitplier)
    total_profit = max_profit(q_star, unit_price, multiplier, fixed_cost)
    
    if total_profit > 0:
        q_star = 0
        
        return q_star




# Exercise 2c

def profit_max_q(q_max: float, step:float, unit_price:float, multiplier:float, fixed_cost:float) -> float():
    
    """Calculate the number of units to maximise profit by using a grid search from 0 to q_max)
    
        >>> profit_max_q(1000, 10, 100, 0.10, 2)
        500
        
        
    """
    

    q_list = np.arange(0, q_max, step)
    i_max = 0
    max_profit = 0
    for i in range(len(q_list)):
        q_i = q_list[i]
        profit_i = total_profit(q_i, unit_price, multiplier, fixed_cost)
        if (profit_i > max_profit):
            i_max = i
            max_profit = profit_i
            
    if (max_profit < 0):
        print("No positive value of quantity was profitable.")
        return 0
    else:
        return q_list[i_max]




# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 

    
    



##################################################
# End
##################################################
