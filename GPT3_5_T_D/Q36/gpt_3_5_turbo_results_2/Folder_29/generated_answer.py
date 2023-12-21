
def filter_chars(string):
    chars_to_remove = set(string[46:68]) - set('Hs')
    return ''.join(char for char in string if char not in chars_to_remove)
