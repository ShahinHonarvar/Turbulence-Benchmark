
def filter_chars(string):
    for i in range(70, 74):
        if 'A' < string[i] < 'U':
            string = string.replace(string[i], '')
    return string
