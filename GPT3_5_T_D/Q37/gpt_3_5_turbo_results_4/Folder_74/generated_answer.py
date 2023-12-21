
def filter_chars(string):
    for i in range(19, 33):
        if 'f' <= string[i] <= 'o':
            string = string.replace(string[i], '')
    return string
