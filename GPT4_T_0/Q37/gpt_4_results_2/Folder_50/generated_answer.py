
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 71 <= i <= 96 and '_' <= c <= 'o'])
    return ''.join([c for c in s if c not in chars_to_remove])
