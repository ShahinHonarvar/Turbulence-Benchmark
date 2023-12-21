
def filter_chars(string):
    for char in string[5:7]:
        if 'G' <= char <= 'p':
            string = string.replace(char, '')
    return string
