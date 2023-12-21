
def filter_chars(s):
    chars_to_remove = set([c for c in s[23:90] if 'w' <= c <= '{'])
    return ''.join([c for c in s if c not in chars_to_remove])
