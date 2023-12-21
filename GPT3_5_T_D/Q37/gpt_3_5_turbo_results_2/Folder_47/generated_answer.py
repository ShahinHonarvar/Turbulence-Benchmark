
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not(38 <= i <= 54 and ':' <= c <= 'r'))
