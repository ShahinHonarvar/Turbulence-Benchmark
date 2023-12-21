
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (2 <= i <= 3 and '5' <= c <= '_')])
