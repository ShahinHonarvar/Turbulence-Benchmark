
def filter_chars(string):
    new_string = ''
    for i in range(1, 7):
        if string[i] > '-' and string[i] < 'L':
            new_string += string[:i] + string[i+1:]
    return new_string
