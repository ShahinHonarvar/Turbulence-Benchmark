
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if not (379 <= i <= 898 and 'M' <= c <= 'v'))
