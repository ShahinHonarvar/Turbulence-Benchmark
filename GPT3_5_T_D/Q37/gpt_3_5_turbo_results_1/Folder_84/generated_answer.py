
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if not (138 <= i <= 920 and '6' <= c <= 'A'))
