
def filter_chars(string):
    for char in string[86:93]:
        if 'E' < char < '~':
            string = string.replace(char, '')
    return string
