
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 69 or i > 80 or char < '@' or char > 'p':
            new_string += char
    return new_string
