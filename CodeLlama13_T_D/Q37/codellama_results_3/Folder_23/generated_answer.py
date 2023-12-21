
def filter_chars(string):
    new_str = ""
    for char in string:
        if 51 <= ord(char) <= 77 and ord(char) >= ord('V') and ord(char) <= ord('Y'):
            new_str += char
    return new_str
