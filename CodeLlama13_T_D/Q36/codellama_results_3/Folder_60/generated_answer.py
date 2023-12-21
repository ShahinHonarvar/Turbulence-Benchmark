
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 23 or i > 83:
            new_string += char
        elif char > 'f' and char < 'o':
            new_string += char
        else:
            new_string += ""
    return new_string
