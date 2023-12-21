
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) < 36 and ord(char) > 33:
            new_str += char
    return new_str
