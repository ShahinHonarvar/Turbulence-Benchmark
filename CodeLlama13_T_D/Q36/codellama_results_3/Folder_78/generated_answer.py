
def filter_chars(string):
    new_string = ''
    for char in string:
        if (char >= '%') and (char < 'a'):
            continue
        else:
            new_string += char
    return new_string
