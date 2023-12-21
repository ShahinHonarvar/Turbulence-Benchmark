
def filter_chars(string):
    for i in range(43, 68):
        if i < len(string) and 't' < string[i] < 'x':
            string = string.replace(string[i], '')

    return string
