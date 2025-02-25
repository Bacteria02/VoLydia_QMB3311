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
from typing import List



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
import math

def logit(x, beta_0, beta_1): # expected input/output (-2)
    
    """ The logit link function transform a probability value (or an 
    independent variable) into a log-odds scale, which is commonly used 
    in logistic regression and statistical modeling.
    
    Create a logit function to calculate the logit transformation using 
    the given values of x, beta0 and beta1.
    
            Parameters:
            x (float): The input value.
            beta_0 (float): The intercept parameter.
            beta_1 (float): The slope parameter.
        
            Returns:
            float: The probability that y = 1 given x.
    
    >>> x = math.log(2)
        beta_0 = 0
        beta_1 = 1
        Ans: 0.667
        
        x = 5
        beta_0 = math.log(3)
        beta_1 = 0
        Ans: .7500
        
        x = math.log(4)
        beta_0 = math.log(1)
        beta_1 = 3
        Ans:0.9846
    """
    # example cases are in incorrect format (-2)
    
    exponent = beta_0 + x * beta_1
    probability = math.exp(exponent) / (1 + math.exp(exponent))
    return probability

#Exercise 1d
def logit_like(yi, xi, beta0, beta1): # expected input/output (-2)

    """Create a log-likelihood to calculate the observation of yi and xi,
        given the parameter of beta1 and beta0 and it's used to estimate
        the logistic regression.
        
        Calculate the log-likelihood of an observation (y_i, x_i).

        Parameters:
        y_i (int): The observed outcome (0 or 1).
        x_i (float): The input value.
        beta_0 (float): The intercept parameter.
        beta_1 (float): The slope parameter.
    
        Returns:
        float: The log-likelihood of the observation.
        
    >>> xi = 2
        yi = 1
        beta0 = 0
        beta1 = 1
        Ans:-0.1269
               
        xi = 1
        yi = 0
        beta0 = 0
        beta1 = 1
        Ans: -1.3133
        
        xi = 1
        yi = 1
        beta0 = 0
        beta1 = 1
        Ans: -0.3133
    >>>
        
    """
    # incorrect formatting of examples (-2)
    
    probability = logit(xi, beta0, beta1)

    if yi == 1:
        log_likelihood = math.log(probability)
    elif yi == 0:
        log_likelihood = math.log(1 - probability)
    else:
        print("Error! yi must be 0 or 1")

    return log_likelihood

def logit_like_sum(y:list[int],x:list[float],beta_0:float,beta_1:float) -> float:
    """Calculates the sum of the log-likelihood across all observation (yi, xi, i=1,...,n)
    y: Binary response variable of either 1 or 0, for each observation
    x: Predictor variable values for each observation
    beta_0: Intercept parameter
    beta_1: Slope parameter
    
    >>>logit_like_sum([1], [1.5], 2, 1)
    -0.02975
    >>>logit_like_sum([0], [2], 1, 2)
    -5.007
    >>>logit_like_sum([1], [5], 3, 3)
    -1.523
    """
    log_likelihood = 0
    for i in range(len(y)):
        log_likelihood += logit_like(y[i],x[i],beta_0,beta_1)
        
    return log_likelihood

#Testing space
y_test= [#input y value]
x_test= [#input x value]
beta0_test= #input beta 0
beta1_test= #input beta 1

like_sum = logit_like_sum(y_test, x_test, beta0_test, beta1_test)
print(f"The logit like sum is: {like_sum}")






#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------


# Exercise 6


def max_logit(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    # Code goes here.
    
    return None




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
