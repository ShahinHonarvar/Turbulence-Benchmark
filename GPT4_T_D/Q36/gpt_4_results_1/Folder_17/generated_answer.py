
def filter_chars(string):
    for char in string[19:95]:
        if 'K' < char < 'a':
            string = string.replace(char, '')
    return string
