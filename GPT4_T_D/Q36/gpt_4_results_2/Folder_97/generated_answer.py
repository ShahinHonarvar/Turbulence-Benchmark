
def filter_chars(s):
    filter_range = set(s[310:591])
    filter_chars = {c for c in filter_range if 'S' < c < 'm'}
    for c in filter_chars:
        s = s.replace(c, '')
    return s
