
def filter_chars(s):
    chars_to_remove = set([c for c in s[10:70] if 'I' <= c <= 'K'])
    return ''.join([c for c in s if c not in chars_to_remove])
