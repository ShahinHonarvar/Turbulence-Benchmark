
def filter_chars(s):
    chars_to_remove = set([c for c in s[722:833] if 'K' <= c <= 'm'])
    return ''.join([c for c in s if c not in chars_to_remove])
