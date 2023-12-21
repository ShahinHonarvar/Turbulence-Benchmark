
def filter_chars(string):
    for char in string[55:66]:
        if 'f' < char < '|':
            string = string.replace(char, '')
    return string
