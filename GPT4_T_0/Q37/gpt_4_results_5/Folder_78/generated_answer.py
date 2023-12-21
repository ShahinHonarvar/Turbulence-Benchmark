
def filter_chars(s):
    chars_to_remove = set([c for c in s[75:100] if '8' <= c <= 'e'])
    return ''.join([c for c in s if c not in chars_to_remove])
