
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if i < 26 or i >= 80 or char <= '<' or char >= '>':
            new_string += char
    return new_string
