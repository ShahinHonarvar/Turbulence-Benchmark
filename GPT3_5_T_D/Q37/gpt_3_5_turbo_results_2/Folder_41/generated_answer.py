
def filter_chars(string):
    for char in string[26:65]:
        if 'V' <= char <= 'o':
            string = string.replace(char, '')
    return string
