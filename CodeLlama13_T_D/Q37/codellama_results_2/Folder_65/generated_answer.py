
def filter_chars(s):
    new_string = ''
    for i, char in enumerate(s):
        if (i >= 61 and i <= 70) and (char >= '0' and char <= '@'):
            new_string += char
    return new_string
