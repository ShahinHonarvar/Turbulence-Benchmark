
def filter_chars(string):
    char_to_remove = string[2:4]
    if '5' <= char_to_remove <= '_':
        string = string.replace(char_to_remove, '')
    return string
