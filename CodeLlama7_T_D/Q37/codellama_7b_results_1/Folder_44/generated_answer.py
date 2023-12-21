
def filter_chars(my_string):
    # Remove all occurrences of characters between indices 21 and 43, both inclusive, that are greater than or equal to '+' and smaller than or equal to '8'
    return "".join([c for c in my_string if (ord(c) < ord('+')) or (ord(c) > ord('8'))])
