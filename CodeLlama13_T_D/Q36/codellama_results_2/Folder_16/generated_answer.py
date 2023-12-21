
def filter_chars(string):
    chars = []
    for i in range(331, 713):
        if string[i] > 'M' and string[i] < '_':
            chars.append(string[i])
    for char in chars:
        string = string.replace(char, '')
    return string
