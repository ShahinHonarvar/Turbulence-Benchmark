
def filter_chars(string):
    new_string = ''
    for char in string:
        if char >= 'X' and char <= 'p':
            new_string += char
    return new_string
