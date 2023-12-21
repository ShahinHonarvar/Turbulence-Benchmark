
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 19 <= i <= 90 and 'F' <= c <= 'h'])
    return ''.join([c for c in s if c not in chars_to_remove])
