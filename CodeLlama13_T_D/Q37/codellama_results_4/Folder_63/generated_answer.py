
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) >= 42 and ord(char) <= 92 and ord(char) >= ord('/') and ord(char) <= ord('a'):
            new_str += char
    return new_str
