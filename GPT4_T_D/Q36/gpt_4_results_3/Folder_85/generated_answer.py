
def filter_chars(string):
    for char in string[56:80]:
        if 'S' < char < 's':
            string = string.replace(char, '')
    return string
