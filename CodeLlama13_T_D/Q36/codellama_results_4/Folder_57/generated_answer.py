
def filter_chars(string):
    for i in range(70, 75):
        char = string[i]
        if 'A' < char < 'U':
            string = string.replace(char, '')
    return string
