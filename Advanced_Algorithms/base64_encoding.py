#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:32:00 2019

@author: tanyallanas
"""

base_64 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
           8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
           16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
           23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd',
           30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k',
           37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r',
           44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
           51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5',
           58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'}


def chunks(string, n):
    """A generator which efficiently splits a string into equal chunks"""
    for i in range(0, len(string), n):
        yield string[i:i + n]


def to_num(string, base):
    """Returns the decimal value of a binary integer"""

    integers = list(map(int, list(string)))
    sum = 0

    for pair in enumerate(integers):
        sum += pair[1]*2**(base - pair[0])

    return sum


def to_binary(num):
    """Returns a binary integer value without the 0b at the beginning"""
    binary = bin(num)[2:]
    actual = len(binary)

    if actual != 8:
        additional = 8 - actual
        return '0'*additional + binary

    return binary


def to_base64(str):
    """Returbs a string in its base 64 representation"""
    to_check = list(str)

    ### -----------------------------------------------------------------------
    ### The following procedure done step-by-step
    ### -----------------------------------------------------------------------
    
    # Find ascii values
    ascii = [ord(item) for item in to_check]
    # Convert to binary values
    binary = [to_binary(item) for item in ascii]
    # Join binary values into string
    binary_string = ''.join(binary)
    # Split into even, 6 digit long chunks
    split = list(chunks(binary_string, 6))
    # Convert chunks to Base64 values
    at_last = [to_num(solution, 5) for solution in split]
    
    ### -----------------------------------------------------------------------
    ### Step-wise parsing ends
    ### -----------------------------------------------------------------------

    return ''.join([base_64.get(number) for number in at_last])