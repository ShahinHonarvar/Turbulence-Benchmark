
def filter_chars(s):
    chars_to_remove = set([c for i, c in enumerate(s) if 513 <= i <= 877 and '?' <= c <= 'n'])
    return ''.join([c for c in s if c not in chars_to_remove])
