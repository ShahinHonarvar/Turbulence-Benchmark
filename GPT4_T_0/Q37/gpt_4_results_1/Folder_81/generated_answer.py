
def filter_chars(s):
    chars_to_remove = set([c for c in s[19:93] if '8' <= c <= 'm'])
    return ''.join([c for c in s if c not in chars_to_remove])
