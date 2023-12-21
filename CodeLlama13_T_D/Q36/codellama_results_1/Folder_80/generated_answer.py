
def filter_chars(s):
    new_string = ''
    for i, char in enumerate(s):
        if i < 54 or i > 92:
            new_string += char
        elif ord(char) <= ord('J') or ord(char) >= ord('X'):
            new_string += char
    return new_string
