
def filter_chars(string):
    for i in range(21, 25):
        if '5' < string[i] < '}':
            string = string.replace(string[i], '')
    return string
