
def filter_chars(string):
    for char in string[53:88]:
        if '&' < char < 'c':
            string = string.replace(char, '')
    return string
