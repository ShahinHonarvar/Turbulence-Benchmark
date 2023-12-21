
def filter_chars(s):
    char_range = set([char for char in s[227:236] if 'D' <= char <= 'u'])
    return ''.join([char for char in s if char not in char_range])
