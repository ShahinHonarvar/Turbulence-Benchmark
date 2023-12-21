
def filter_chars(string):
    new_string = ''
    for char in string:
        if char < 'J' or char > 'Q':
            new_string += char
    return new_string
