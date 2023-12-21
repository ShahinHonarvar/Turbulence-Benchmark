
def filter_chars(string):
    for char in string[32:47]:
        if '0' <= char <= 'k':
            string = string.replace(char, '')
    return string
