
def filter_chars(string):
    for i in range(55, 66):
        if 'f' < string[i] < '|':
            string = string.replace(string[i], '')
    return string
