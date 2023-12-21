
def filter_chars(string):
    chars_to_remove = set(string[58:81]) - set('6:>?')
    return ''.join(char for char in string if char not in chars_to_remove)
