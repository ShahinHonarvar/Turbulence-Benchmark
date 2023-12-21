
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i >= 38 and i <= 99 and char >= 'A' and char <= 'Q':
            continue
        new_string += char
    return new_string
