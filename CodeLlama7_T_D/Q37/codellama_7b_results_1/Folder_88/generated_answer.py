
def filter_chars(string):
    for i in range(69, 81):
        if string[i] >= '@' and string[i] <= 'p':
            string = string.replace(string[i], '', 1)
    return string
