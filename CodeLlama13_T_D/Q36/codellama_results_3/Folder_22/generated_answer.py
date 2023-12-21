
def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if 55 <= ord(char) <= 84 and char != ';' and char != 'z':
            new_string += char
        else:
            new_string += string[i]
    return new_string
