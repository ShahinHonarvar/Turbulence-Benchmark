
def filter_chars(string):
    for char in string[1:6]:
        if ',' < char < 'f':
            string = string.replace(char, '')
    return string
