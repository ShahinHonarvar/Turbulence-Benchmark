
def filter_chars(string):
    new_str = ''
    for char in string:
        if ord(char) > ord('#') and ord(char) < ord('L'):
            new_str += char
    return new_str
