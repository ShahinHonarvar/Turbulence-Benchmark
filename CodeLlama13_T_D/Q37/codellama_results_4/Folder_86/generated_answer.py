
def filter_chars(string):
    new_str = ""
    for char in string:
        if ord(char) >= 164 and ord(char) <= 706 and ord(char) >= ord('O') and ord(char) <= ord('}'):
            new_str += char
        else:
            new_str += char
    return new_str
