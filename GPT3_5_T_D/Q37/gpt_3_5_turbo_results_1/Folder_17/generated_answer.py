
def filter_chars(string):
    for i in range(27, 30):
        if ';' <= string[i] <= 'b':
            string = string.replace(string[i], '')
    return string
