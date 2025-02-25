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
def CESutility(good_x: float, good_y: float, r: float) -> float:
    """Calculate the constant elasticity of subsitution utility function for two goods.
    
    >>> CESutility(3, 4, 2)
    5.0
    >>> CESutility(1, 1, 2)
    1.4142135623730951
    >>> CESutility(3**0.5, 4**0.5, 4)
    2.23606797749979
    """
    
    utility = (good_x**r + good_y**r)**(1/r)
    return utility

def CESutility_valid(x: float, y: float, r: float) -> float:
   
    """Return the value of the constant elasticity of substitution utitlity
    function to determine the satistfaction of two goods of x and y. R is
    the parameter that determines the curvature of the indifference curves.
    x: Quantity of good1 (must be non-negative).
    y: Quantity of good2 (must be non-negative).
    r: Substitution parameter (must be strictly positive).

    >>> CESutility_valid(5, 5, 0.5)
        20.0
    >>> CESutility_valid(5, -3, 0.5)
        None (Non-eligible input, quantity of good 2 (y) must be non-negative.)
    >>> CESutility_valid(5, 3, -0.5)
        None (Non-eligible input, the substitution parameter (r) must be strictly positive.)
    """
    if x < 0:
        print("Non-eligible input, quantity of good1 (x) must be non-negative.")
        return None
    if y < 0:
        print("Non-eligible input, quantity of good 2 (y) must be non-negative.")
        return None
    if r <= 0:
        print("Non-eligible input, the substitution parameter (r) must be strictly positive.")
        return None
    
    
    return CESutility(x,y,r)

def CESutility_in_budget(x: float, y: float, r: float, 
                         p_x: float, p_y: float, w: float) -> float:
    
    """Return the value of the constant elasticity of substitution utitlity
    function to determine the satistfaction of two goods of x and y. R is
    the parameter that determines the curvature of the indifference curves.
    Testing under budget constraint w. 
    x: Quantity of good1 (must be non-negative).
    y: Quantity of good2 (must be non-negative).
    r: Substitution parameter (must be strictly positive)
    p_x: Price of good1 (x) 
    p_y: Price of good2 (y) 
    w: Consumer wealth (budget constraint)
    
    >>>CESutility_in_budget(5, 7, 0.4, 3, 3, 50)
    33.66
    >>>CESutility_in_budget(10, 15, 0.5, 7, 8, 40)
    None (Consumer's basket of goods not within set budget constraint (w). Cost of Basket: 190, Budget: 40)
    >>>CESutility_in_budget(3, 3, -0.6, 2, 3, 45)
    None (Non-eligible input, the substitution parameter (r) must be strictly positive.)
    """
    
    # Check budget constraint first. 
    if p_x*x + p_y*y > w:
        print('Error in CESutility_in_budget: budget constraint not satisfied.')
        return None
    else :
        # If budget constraint is satisfied, call the CESutility_valid function. 
        utility = CESutility_valid(x, y, r)
        return utility
    

#--------------------------------------------------
# Question 2e
# New Functions

def max_CES_util(x_min: float, x_max: float, y_min: float, y_max:float, step:float, r:float, p_x: float, p_y: float, w:float) - > float:
        """ Calculate the derive utility from good x and good y to maximise the constant elast of substitution.


         >>> max_CES_util(0, 12/2, 0, 12/4, 0.1, 1/2, 2, 4, 12)
             9.0
         >>> max_CES_util(0, 12/3, 0, 12/2, 0.1, 1/2, 2, 5, 12)
             20.0
        >>> max_CES_util_v2(0, 2/1, 0, 2/1, 0.01, 2, 1, 1, 2)
             1.978

    
        """
        x_ star = max_CES_xy(x_min, x_max, y_min, y_max, step, 
            r, p_x, p_y, w)
        
        y_star = max_CES_xy(x_min, x_max, y_min, y_max, step, 
            r, p_x, p_y, w)
        
        max_uti_CES = CESutility_in_budget(xy_star[0], xy_star[1], r, p_x, p_y, w)
        
        return max_uti_CES

#--------------------------------------------------

# Exercise 4


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
