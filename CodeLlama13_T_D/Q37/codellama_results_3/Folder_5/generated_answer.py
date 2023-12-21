
def filter_chars(string):
    new_str = ''
    for i in range(24, 83):
        char = string[i]
        if ord(char) >= 5 and ord(char) <= 60:
            new_str += char
    return new_str
