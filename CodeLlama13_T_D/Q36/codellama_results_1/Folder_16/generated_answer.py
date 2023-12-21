
def filter_chars(string):
    for i in range(331, 713):
        if string[i].isalpha() and string[i] > 'M' and string[i] < '_':
            string = string.replace(string[i], '')
    return string
