
def filter_chars(string):
    for char in string[20:69]:
        if '<' < char < 'C':
            string = string.replace(char, '')
    return string
