
def filter_chars(string):
    new_string = ''
    for index, char in enumerate(string):
        if 344 <= index < 874 and 'f' < char < '~':
            continue
        new_string += char
    return new_string
