
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 35 <= i <= 40 and ')' <= char <= 'l':
            continue
        new_string += char
    return new_string
