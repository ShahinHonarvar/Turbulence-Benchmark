
def filter_chars(string):
    for i in range(55, 84):
        if string[i].isalpha() and string[i] > ';' and string[i] < 'z':
            string = string.replace(string[i], '')
    return string
