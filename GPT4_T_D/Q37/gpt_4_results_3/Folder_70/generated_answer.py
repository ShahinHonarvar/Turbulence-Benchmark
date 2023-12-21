
def filter_chars(s):
    filter = set([c for c in s[515:539] if '+' <= c <= '}'])
    return ''.join([c for c in s if c not in filter])
