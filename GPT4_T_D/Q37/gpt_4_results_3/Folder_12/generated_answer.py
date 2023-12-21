
def filter_chars(string):
    temp_set = set([c for c in string[19:91] if 'F' <= c <= 'h'])
    
    new_string = ''
    for char in string:
        if char not in temp_set:
            new_string += char
    
    return new_string
