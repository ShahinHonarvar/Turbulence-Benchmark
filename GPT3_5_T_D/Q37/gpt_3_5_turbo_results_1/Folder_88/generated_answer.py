
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i < 69 or i > 80 or string[i] < '@' or string[i] > 'p':
            new_string += string[i]
            
    return new_string
