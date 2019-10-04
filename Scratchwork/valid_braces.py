#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:13:41 2019

@author: tanyallanas
"""

from collections import Counter
from itertools import islice

def braces_are_pair(current, previous):
    """Checks whether two input braces are a correctly matched pair"""
    
    if current == ')' and previous == '(':
        return True
    
    elif current == ']' and previous == '[':
        return True
    
    elif current == '}' and previous == '{':
        return True
    
    else:
        return False

def all_braces_matched(string_list):
    """ Returns True if all of the braces in a string are correctly matched,
    False otherwise
    """
    tracker = [string_list[0]]
    
    for brace in islice(string_list, 1, None):

        if len(tracker) != 0:
            
            if braces_are_pair(brace, tracker[-1]):
                del tracker[-1]
                
            else:
                tracker.append(brace)
                
        else:
            tracker.append(brace)
            continue
        
    if len(tracker) == 0:
        return True
    
    return False
            
        

def validBraces(string):
    """ Wrapper function, calls all_braces_matched() to determine whether the
    braces in the input string are all correctly matched
    """
    pairs_exist = Counter(list(string))

    if pairs_exist['{'] == pairs_exist['}'] and pairs_exist['['] == pairs_exist[']'] and pairs_exist['('] == pairs_exist[')']:
        string_list = list(string)
        
        return all_braces_matched(string_list)

    return False