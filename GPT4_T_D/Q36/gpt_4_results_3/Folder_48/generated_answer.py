
def filter_chars(string):
    for char in string[155:222]:
        if 'A' < char < 'f':
            string = string.replace(char, '')
    return string
