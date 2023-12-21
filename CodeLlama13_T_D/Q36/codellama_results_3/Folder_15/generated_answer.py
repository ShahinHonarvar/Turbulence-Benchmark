
def filter_chars(string):
    new_string = ''
    for i, c in enumerate(string):
        if (i < 2 or i > 7) and c not in 'hk':
            new_string += c
    return new_string
