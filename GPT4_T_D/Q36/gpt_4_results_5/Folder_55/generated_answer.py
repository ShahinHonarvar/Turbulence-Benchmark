
def filter_chars(string):
    for i in range(4, 5):
        if 'Y' < string[i] < 's':
            string = string.replace(string[i], '')
    return string
