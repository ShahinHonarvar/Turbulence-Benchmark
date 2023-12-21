
def filter_chars(string):
    for char in string[11:15]:
        if 't' < char < 'v':
            string = string.replace(char, '')
    return string
