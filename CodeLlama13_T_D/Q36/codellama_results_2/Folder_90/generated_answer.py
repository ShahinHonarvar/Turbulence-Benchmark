
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 344 <= ord(char) <= 874 and char != 'f' and char != '~':
            continue
        new_str += char
    return new_str
