
def filter_chars(string):
    for char in string[24:83]:
        if 'f' < char < 'o':
            string = string.replace(char, '')
    return string
