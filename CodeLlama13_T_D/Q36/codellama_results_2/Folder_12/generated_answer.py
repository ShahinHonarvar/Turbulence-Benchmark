
def filter_chars(s):
    new_string = ""
    for char in s:
        if 32 <= ord(char) < 84 and char > 'm' and char < 'w':
            new_string += char
        else:
            new_string += char
    return new_string
