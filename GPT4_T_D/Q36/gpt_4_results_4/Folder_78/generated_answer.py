
def filter_chars(string):
    for char in string[30:33]:
        if '%' < char < 'a':
            string = string.replace(char, '')
    return string
