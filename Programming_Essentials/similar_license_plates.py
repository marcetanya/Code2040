#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:41:58 2019

@author: tanyallanas
"""

similar_letters = {'0': ('O', 'Q'), 'O': ('0', 'Q'), 'Q': ('0', 'O'),
                   '1': ('I', 'T'), 'I': ('1', 'T'), 'T': ('1', 'I'),
                   '2': ('Z',), 'Z': ('2',), '5': ('S',), 'S': ('5',),
                   '8': ('B',), 'B': ('8',)}

def similar_license_plates(plate1, plate2, similar=True):
    """
    Given a dictionary mapping similar letters to each other, returns true if
    two license plates are visually similar, otherwise returns false.
    Assumes the two license plates are the same length.
    """
    plate1 = plate1.replace(' ', '')
    plate2 = plate2.replace(' ', '')

    # Case 1: License plates identical
    if plate1 == plate2:
        return similar
    
    # Case 2: License plates are not identical; iterate through license plates
    # characters
    for i in range(len(plate1)):
        
        # Case 2.1: Current character is the same
        if plate1[i] == plate2[i]:
            pass
        
        # Case 2.2: Current character not the same, but potentially similar
        elif plate1[i] in similar_letters:
            if plate2[i] not in similar_letters.get(plate1[i]):
                similar = False
                break
            
        # Case 2.3: Current characters are not the same and not potentially similar
        elif plate1[i] != plate2[i]:
            similar = False
            
    return similar