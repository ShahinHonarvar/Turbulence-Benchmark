
def filter_chars(s):
    chars_to_remove = set([c for c in s[24:80] if 'a' <= c <= 'f'])
    return ''.join([c for c in s if c not in chars_to_remove])
