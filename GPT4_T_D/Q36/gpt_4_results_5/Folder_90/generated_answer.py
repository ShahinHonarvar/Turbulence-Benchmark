
def filter_chars(string):
    char_set = set([char for char in string[345:874] if 'f' < char < '~'])
    for char in char_set:
        string = string.replace(char, '')
    return string
