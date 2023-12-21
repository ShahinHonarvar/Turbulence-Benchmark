
def filter_chars(string):
    chars_to_remove = list(set(string[46:86]) & set('-ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    return ''.join([char for char in string if char not in chars_to_remove])
