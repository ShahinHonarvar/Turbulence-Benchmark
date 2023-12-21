
def filter_chars(string):
    for char in string[45:68]:
        if 'W' < char < 'x':
            string = string.replace(char, '')
    return string
