
def filter_chars(string):
    new_string = ""
    for i in range(1, 6):
        if string[i] > ',' and string[i] < 'f':
            new_string += string[:i-1] + string[i:]
    return new_string
