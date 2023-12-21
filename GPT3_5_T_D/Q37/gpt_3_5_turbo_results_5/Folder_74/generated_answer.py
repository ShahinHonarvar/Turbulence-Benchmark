
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if not (19 <= i <= 32 and 'f' <= c <= 'o'))
