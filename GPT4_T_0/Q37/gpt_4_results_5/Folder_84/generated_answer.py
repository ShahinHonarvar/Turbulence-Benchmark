
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 138 <= i <= 920 and '6' <= c <= 'A'])
    return ''.join([c for c in s if c not in chars_to_remove])
