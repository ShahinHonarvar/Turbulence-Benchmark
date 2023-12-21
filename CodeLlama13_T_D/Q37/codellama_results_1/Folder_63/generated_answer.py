
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) < 92 and ord(char) > 41 and char != '/':
            new_str += char
    return new_str
