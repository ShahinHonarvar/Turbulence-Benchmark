
def filter_chars(s):
    chars_to_remove = set([c for c in s[38:55] if ':' <= c <= 'r'])
    return ''.join([c for c in s if c not in chars_to_remove])
