
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 31 < ord(char) <= 70:
            new_string += char
    return new_string
