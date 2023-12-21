
def filter_chars(string):
    for i in range(1, 6):
        if ',' < string[i] < 'f':
            string = string.replace(string[i], '')
    return string
