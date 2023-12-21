
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 86 <= ord(char) <= 93 and char > 'E' and char < '~':
            new_str += char
    return new_str
