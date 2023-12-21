
def filter_chars(string):
    for i in range(31, 39):
        if string[i] >= ';' and string[i] <= 'g':
            string = string.replace(string[i], '')
    return string
