
def filter_chars(string):
    new_str = ''
    for char in string:
        if ord(char) < 138 or ord(char) > 920 or (ord(char) >= 6 and ord(char) <= 71):
            new_str += char
    return new_str
