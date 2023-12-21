

def filter_chars(string):
    new_string = ''
    for index, char in enumerate(string):
        if index < 344 or index >= 874:
            new_string += char
        elif char > 'f' and char < '~':
            continue
        else:
            new_string += char
    return new_string
