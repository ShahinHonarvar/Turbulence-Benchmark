
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (5 <= i <= 6 and 'G' <= c <= 'p'))
