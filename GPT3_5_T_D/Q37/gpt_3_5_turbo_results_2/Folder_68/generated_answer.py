
def filter_chars(string):
    for char in string[7:10]:
        if '6' <= char <= 'w':
            string = string.replace(char, '')
    return string
