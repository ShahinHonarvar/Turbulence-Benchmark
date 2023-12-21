
def filter_chars(s):
    filter_set = set([c for i, c in enumerate(s) if 27 <= i <= 85 and 'c' <= c <= 'i'])
    return ''.join([c for c in s if c not in filter_set])
