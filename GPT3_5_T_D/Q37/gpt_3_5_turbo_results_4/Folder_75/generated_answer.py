
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (34 <= i <= 67 and 'W' <= c <= 'x'))
