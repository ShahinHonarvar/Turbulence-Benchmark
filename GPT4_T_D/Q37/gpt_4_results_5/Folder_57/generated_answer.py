
def filter_chars(string):
    for char in string[27:86]:
        if '!' <= char <= 'B':
            string = string.replace(char, '')
    return string
