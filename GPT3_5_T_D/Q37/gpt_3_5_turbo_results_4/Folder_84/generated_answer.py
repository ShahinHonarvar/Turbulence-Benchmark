
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (138 <= i <= 920 and '6' <= c <= 'A'))
