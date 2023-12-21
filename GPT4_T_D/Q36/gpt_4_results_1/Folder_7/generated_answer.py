
def filter_chars(s):
    chars_to_remove = set([char for char in s[503:946] if 'W' < char < 'y'])
    return ''.join([char for char in s if char not in chars_to_remove])
