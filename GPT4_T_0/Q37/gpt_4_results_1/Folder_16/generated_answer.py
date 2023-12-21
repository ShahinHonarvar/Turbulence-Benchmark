
def filter_chars(s):
    chars_to_remove = set([c for c in s[225:382] if 'D' <= c <= 'Y'])
    return ''.join([c for c in s if c not in chars_to_remove])
