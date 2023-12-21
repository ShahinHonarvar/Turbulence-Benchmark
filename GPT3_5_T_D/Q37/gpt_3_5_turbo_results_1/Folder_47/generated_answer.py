
def filter_chars(string):
    new_string = ''
    for i, c in enumerate(string):
        if 37 < i < 55 and ':' <= c <= 'r':
            continue
        new_string += c
    return new_string
