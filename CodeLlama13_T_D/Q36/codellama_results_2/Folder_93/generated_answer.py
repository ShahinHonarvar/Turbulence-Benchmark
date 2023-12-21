
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) < 52 or ord(char) > 88:
            new_str += char
    return new_str
