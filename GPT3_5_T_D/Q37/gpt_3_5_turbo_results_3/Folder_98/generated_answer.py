
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (8 <= i <= 9 and 'R' <= c <= 't'))
