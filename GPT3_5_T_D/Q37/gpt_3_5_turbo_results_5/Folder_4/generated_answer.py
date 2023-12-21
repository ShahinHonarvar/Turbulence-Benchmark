
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 19 <= i <= 33 and 'S' <= char <= '{':
            continue
        new_string += char
    return new_string
