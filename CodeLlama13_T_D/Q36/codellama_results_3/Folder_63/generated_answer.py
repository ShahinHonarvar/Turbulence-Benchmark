
def filter_chars(string):
    new_str = ''
    for i, c in enumerate(string):
        if i < 26 or i > 80:
            new_str += c
        elif c < '>' and c > '<':
            new_str += c
        else:
            new_str += string.replace(c, '')
    return new_str
