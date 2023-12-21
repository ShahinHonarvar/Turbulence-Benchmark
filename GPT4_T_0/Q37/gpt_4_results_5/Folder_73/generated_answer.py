
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 22 <= i <= 85 and '7' <= c <= 'e'])
    return ''.join([c for c in s if c not in chars_to_remove])
