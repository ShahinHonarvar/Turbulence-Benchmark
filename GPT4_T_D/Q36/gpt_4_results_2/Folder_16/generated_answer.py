
def filter_chars(s):
    chars_to_remove = set([c for c in s[332:713] if 'M' < c < '_'])
    return ''.join([c for c in s if c not in chars_to_remove])
