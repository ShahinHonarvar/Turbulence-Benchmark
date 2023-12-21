
def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (318 <= i < 337 and 'B' < c < 'z')])
