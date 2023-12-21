
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 34 <= i <= 67 and 'W' <= char <= 'x':
            continue
        new_string += char
    return new_string
