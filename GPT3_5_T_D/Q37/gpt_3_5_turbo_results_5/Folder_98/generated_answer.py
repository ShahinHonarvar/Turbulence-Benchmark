
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 8 or i > 9 or string[i] < 'R' or string[i] > 't':
            new_string += string[i]
    
    return new_string
