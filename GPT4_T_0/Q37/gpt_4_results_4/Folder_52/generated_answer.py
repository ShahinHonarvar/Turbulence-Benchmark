
def filter_chars(s):
    chars_to_remove = set([c for c in s[54:84] if 'j' <= c <= 'v'])
    return ''.join([c for c in s if c not in chars_to_remove])
