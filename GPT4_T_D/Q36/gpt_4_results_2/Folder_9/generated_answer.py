
def filter_chars(string):
    for char in set(string[51:92]):
        if 'A' < char < 'Q':
            string = string.replace(char, '')
    return string
