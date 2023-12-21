
def filter_chars(string):
    for char in string[12:89]:
        if '&' <= char <= 'v':
            string = string.replace(char, '')
    return string
