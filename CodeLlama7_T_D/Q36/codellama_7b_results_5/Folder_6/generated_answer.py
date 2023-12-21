
def filter_chars(string):
    for i in range(31, 70):
        if string[i] > 'B' and string[i] < 'v':
            string = string.replace(string[i], '')
    return string
