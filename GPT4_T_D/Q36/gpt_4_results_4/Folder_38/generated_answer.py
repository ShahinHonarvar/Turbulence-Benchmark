
def filter_chars(s):
    # create list of chars to be removed
    chars_to_remove = [char for char in s[45:48] if '+' < char < 'l']
    
    # remove each char from string and update the string
    for char in chars_to_remove:
        s = s.replace(char, '')
    
    return s
