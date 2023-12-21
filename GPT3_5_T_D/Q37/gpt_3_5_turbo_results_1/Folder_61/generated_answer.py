
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i > 4 and i < 7 and 'G' <= char <= 'p':
            continue
        new_string += char
    return new_string
