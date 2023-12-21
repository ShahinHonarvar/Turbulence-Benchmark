
def filter_chars(string):
    for char in string[45:59]:
        if '/' < char < '6':
            string = string.replace(char, '')
    return string
