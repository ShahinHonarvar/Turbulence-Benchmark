
def filter_chars(s):
    char_to_remove = set([c for c in s[227:236] if 'D' <= c <= 'u'])
    return ''.join([c for c in s if c not in char_to_remove])
