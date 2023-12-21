
def filter_chars(string):
    for i in range(41, 56):
        if string[i].isupper() and string[i] < 'c':
            string = string.replace(string[i], '')
    return string
