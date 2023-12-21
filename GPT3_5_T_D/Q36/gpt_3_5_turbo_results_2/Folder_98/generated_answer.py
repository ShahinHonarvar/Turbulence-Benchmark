
def filter_chars(string):
    for i in range(4, 8):
        if '1' < string[i] < 'J':
            string = string.replace(string[i], '')
    return string
