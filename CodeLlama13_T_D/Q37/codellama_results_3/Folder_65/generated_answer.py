
def filter_chars(s):
    new_string = ''
    for i, c in enumerate(s):
        if 61 <= i <= 70 and '0' <= c <= '@':
            continue
        else:
            new_string += c
    return new_string
