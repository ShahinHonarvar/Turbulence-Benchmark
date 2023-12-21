
def filter_chars(s):
    filter_chars_set = {c for c in s[32:47] if '0' <= c <= 'k'}
    return ''.join(c for c in s if c not in filter_chars_set)
