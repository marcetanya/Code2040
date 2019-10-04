def square_digits(num):
    """Squares every digit of a number.
    
    Args:
        num: an integer
        
7   Returns:
        The result of taking every digit of the original number and squaring
        it, then adding the value to the end of a new integer. For example:
            
            num = 9119
            square_digits(num) = 811181
            
        This is because 9 squared is 81 and 1 squared is 1, so (81)(1)(1)(81)
        becomes 811181.
    """
    
    # Turn the number into a string
    iter_num = str(num)
    ret_num = ''
    
    for digit in iter_num:
        # Turn the digit into an integer
        math_digit = int(digit)
        square_num = math_digit * math_digit
        
        # Concatenate the squared number, as a string, to the running string
        ret_num = ret_num + str(square_num)
        
    # Return the final string number as an integer
    return int(ret_num)