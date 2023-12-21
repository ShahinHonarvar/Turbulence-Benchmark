
def filter_chars(string):
    chars = []
    for i in range(24, 79 + 1):
        if string[i].isalpha() and string[i] >= 'a' and string[i] <= 'f':
            chars.append(string[i])
    for char in chars:
        string = string.replace(char, '')
    return string
