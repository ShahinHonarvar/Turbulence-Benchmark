
def filter_chars(string):
    # Find all characters between indices 54 and 92 (both exclusive)
    chars = set([c for c in string[54:92] if c > 'J' and c < 'X'])
    
    # Remove all occurrences of these characters from the string
    new_string = ""
    for c in string:
        if c not in chars:
            new_string += c
            
    return new_string
