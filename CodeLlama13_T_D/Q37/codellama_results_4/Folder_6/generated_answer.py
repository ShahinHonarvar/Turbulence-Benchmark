
def filter_chars(s):
    new_string = ''
    for i, char in enumerate(s):
        if i < 13 or i > 28 or char < 'c' or char > 'n':
            new_string += char
    return new_string
