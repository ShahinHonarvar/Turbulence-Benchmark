
def filter_chars(string):
    for index in range(86, 93):
        char = string[index]
        if 'E' < char < '~':
            string = string.replace(char, '')
    return string
