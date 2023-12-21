
def filter_chars(string):
    new_str = ''
    for char in string:
        if char >= ';' and char <= 'g':
            new_str += char
    return new_str
