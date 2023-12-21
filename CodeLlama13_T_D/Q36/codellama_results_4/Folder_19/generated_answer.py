
def filter_chars(string):
    new_string = ''
    for i in range(77, 87):
        if string[i] > ';' and string[i] < 'r':
            new_string += string[:i] + string[i+1:]
        else:
            new_string += string[i]
    return new_string
