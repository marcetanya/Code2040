#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:57:36 2019

@author: tanyallanas
"""

def return_num(value):
    """ If a letter, maps value to its corresponding number and returns the
    number.
    If a number, returns value.
    Handles lowercase input.
    """
    hex_letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    return int(hex_letters.get(value, value))

def list_hex_pairs(values):
    """ Returns a list of number pairs representing the hexadecimal channels.
    Paired numbers are represented by tuples.
    """
    return [(return_num(value[0]), return_num(value[1])) for value in values]

def rgb_map(values):
    """ Creates a list of hexadecimal channels represented by number pairs.
    Performs the conversion from hexadecimal to rgb value.
    Returns the parsed color as a map.
    """
    hex_pairs = list_hex_pairs(values)
    rgb_values = [pair[0]*16 + pair[1] for pair in hex_pairs]
    
    return {'r': rgb_values[0], 'g': rgb_values[1], 'b': rgb_values[2]}

def parse_html_color(color):
    """Parses a string representation of a hexadecimal into channels and maps
    these to rgb values.
    Takes a preset color name, locates the string representation of its
    hexadecimal, and then maps to rgb values.
    """
    if color[0] == '#':
    
        if len(color) == 7:
            values = [color[1:3], color[3:5], color[5:7]]
            return rgb_map(values)
        
        elif len(color) == 4:
            # Solve single-digit issue; both digits of the hexadecimal channel
            # are the same
            values = [color[1:2]*2, color[2:3]*2, color [3:4]*2]
            return rgb_map(values)

    else:
        # Note: PRESET_COLORS defined in test suite
        color = PRESET_COLORS.get(color.lower())
        values = [color[1:3], color[3:5], color[5:7]]
        return rgb_map(values)