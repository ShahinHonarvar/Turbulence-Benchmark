
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] < '1' or string[i] > 'J':
            new_string += string[i]
    return new_string
