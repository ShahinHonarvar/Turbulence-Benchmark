
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 13 <= i <= 28 and 'c' <= c <= 'n'])
    return ''.join([c for c in s if c not in chars_to_remove])
