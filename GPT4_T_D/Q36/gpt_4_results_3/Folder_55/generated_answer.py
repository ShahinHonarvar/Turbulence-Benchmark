
def filter_chars(string):
    for char in string[4:5]:
        if 'Y' < char < 's':
            string = string.replace(char, '')
    return string
