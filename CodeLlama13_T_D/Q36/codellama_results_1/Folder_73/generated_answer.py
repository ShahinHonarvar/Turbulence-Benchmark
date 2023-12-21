
def filter_chars(string):
    for i in range(66, 90):
        if string[i] > '#' and string[i] < 'T':
            string = string.replace(string[i], '')
    return string
