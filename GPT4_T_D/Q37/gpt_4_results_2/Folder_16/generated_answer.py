
def filter_chars(string):
    chars_to_remove = set([char for char in string[225:382] if 'D' <= char <= 'Y'])
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
