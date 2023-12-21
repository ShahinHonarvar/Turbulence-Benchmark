
def filter_chars(string):
    for i in string[310:591]:
        if 'S' < i < 'm':
            string = string.replace(i, '')
    return string
