
def filter_chars(s):
    chars_to_filter = set([c for i, c in enumerate(s) if 29 <= i <= 79 and 'K' <= c <= 'z'])
    return ''.join([c for c in s if c not in chars_to_filter])
