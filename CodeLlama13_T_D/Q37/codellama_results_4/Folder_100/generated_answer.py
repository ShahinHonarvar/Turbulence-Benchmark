
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) < 89 or ord(char) > 103:
            new_str += char
    return new_str
