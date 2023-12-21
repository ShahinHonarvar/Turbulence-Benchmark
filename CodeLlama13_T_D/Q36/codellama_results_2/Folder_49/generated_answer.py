
def filter_chars(string):
    new_str = ''
    for char in string:
        if ord(char) < 46 or ord(char) > 91:
            new_str += char
    return new_str
