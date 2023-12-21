
def filter_chars(string):
    chars = string[4:5]
    for char in chars:
        if 'Y' < char < 's':
            string = string.replace(char, '')
    return string
