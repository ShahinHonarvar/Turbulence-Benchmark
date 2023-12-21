
def filter_chars(s):
    chars_to_remove = set([c for c in s[15:56] if 'W' <= c <= '{'])
    return ''.join([c for c in s if c not in chars_to_remove])
