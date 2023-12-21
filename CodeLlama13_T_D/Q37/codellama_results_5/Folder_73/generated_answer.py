
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 22 <= i <= 85 and '7' <= char <= 'e':
            continue
        else:
            new_string += char
    return new_string
