
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i < 171 or i > 636:
            new_string += char
        elif char > 'c' and char < 's':
            new_string += char
        else:
            new_string += ''
    return new_string
