
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (19 <= i <= 32 and 'f' <= c <= 'o')])
