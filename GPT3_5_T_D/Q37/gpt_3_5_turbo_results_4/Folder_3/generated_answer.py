
def filter_chars(string):
    for char in string[37:57]:
        if '6' <= char <= '_':
            string = string.replace(char, '')
    return string
