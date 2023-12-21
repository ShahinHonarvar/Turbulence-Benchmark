
def filter_chars(s):
    char_to_remove = set([c for i, c in enumerate(s) if 603 <= i <= 759 and 'Q' <= c <= 'h'])
    return ''.join([c for c in s if c not in char_to_remove])
