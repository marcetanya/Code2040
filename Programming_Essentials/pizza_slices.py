#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:46:50 2019

@author: tanyallanas
"""

### ---------------------------------------------------------------------------
### Recursive lazy caterer solution below
### ---------------------------------------------------------------------------

#def pizza_recursion(cut):
#    """ Recursively creates the trail of tuples defining the characteristics of
#    the pizza after each cut. Each tuple specifies:
#        
#        (number of cuts [also number of slices cut in two],
#        (number of new slices [number of cut slices times two],
#         untouched slices [number of slices in previous iteration
#                           minus number of cuts],
#         number of total slices [number of new slices plus number
#                                 of untouched slices])
#        
#    Will be wrapped by max_pizza.
#    
#    Note: Recursive solution breaks for large test cases. Non-recursive solution
#    must be found.
#    """
#
#    if cut < 0:
#        return (0, 0, 0, -1)
#    
#    elif cut == 0:
#        return (0, 0, 0, 1)
#    
#    else:
#        # Recursive call below
#        look_back = pizza_recursion(cut-1)[-1]
#        return (cut, cut*2, look_back - cut, cut*2 + look_back - cut)
#
#
#def max_pizza(cut):
#    """Wrapper function for pizza_recursion."""
#    return (pizza_recursion(cut)[-1])

### ---------------------------------------------------------------------------
### Recursive lazy caterer solution above
### ---------------------------------------------------------------------------


def max_pizza(cut):
    """ Solves pizza problem for larger values, n --> 45000, nonrecursively."""
    if cut < 0:
        return -1
    
    return(cut*(cut+1))/2 + 1