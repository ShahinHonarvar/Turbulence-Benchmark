
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 164 <= i <= 706 and 'O' <= c <= '}'])
    return ''.join([c for c in s if c not in chars_to_remove])
