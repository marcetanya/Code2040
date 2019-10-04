def to_camel_case(text):
    """Converts a string to camel case."""
    char_list = []
    # Create reversed iterator
    for char in reversed(text):
        if char == '-' or char == '_':
            # If a letter, replace character before '-' or '_' with uppercase
            if char_list[-1] in 'abcdefghijklmnopqrstuvwxyz':
                char_list[-1] = char_list[-1].upper()
            else:
                char_list.append(char)
    # Reorient list
    char_list.reverse()
    
    return ''.join(char_list)