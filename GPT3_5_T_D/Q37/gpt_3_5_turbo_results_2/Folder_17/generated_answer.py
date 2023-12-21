
def filter_chars(string):
    for char in string[27:30]:
        if ';' <= char <= 'b':
            string = string.replace(char, '')
    return string
