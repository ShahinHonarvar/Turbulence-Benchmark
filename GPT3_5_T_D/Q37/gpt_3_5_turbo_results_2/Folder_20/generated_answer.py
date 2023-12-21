
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 25 <= i <= 97 and 'm' <= char <= 'w':
            continue
        new_string += char
    return new_string
