
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 17 or i > 63 or not ('O' <= c <= '^'))
