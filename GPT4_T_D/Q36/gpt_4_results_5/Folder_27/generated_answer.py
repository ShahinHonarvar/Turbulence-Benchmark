
def filter_chars(s):
    char_set = set([char for char in s[49:75] if char > '6' and char < '_'])
    return ''.join([char for char in s if char not in char_set])
