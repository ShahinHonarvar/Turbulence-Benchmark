
def filter_chars(string):
    for i in range(23, 83):
        if string[i].lower() > 'f' and string[i].lower() < 'o':
            string = string.replace(string[i], '')
    return string
