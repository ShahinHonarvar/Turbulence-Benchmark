
def filter_chars(string):
    for char in string[43:68]:
        if 't' < char < 'x':
            string = string.replace(char, '')
    return string
