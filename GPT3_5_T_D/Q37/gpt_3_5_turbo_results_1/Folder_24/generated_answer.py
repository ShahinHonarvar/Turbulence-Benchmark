
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i >= 36 and i <= 79 and char >= '2' and char <= 's':
            continue
        new_string += char
    return new_string
