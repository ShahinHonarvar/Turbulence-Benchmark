
def filter_chars(string):
    for i in range(2, -1, -1):
        if ('$' < string[i] < '?'):
            string = string.replace(string[i], '')
    return string
