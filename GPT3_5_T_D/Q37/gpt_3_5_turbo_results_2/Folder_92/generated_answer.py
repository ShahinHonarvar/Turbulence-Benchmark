
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (4 <= i <= 4 and '7' <= c <= 'o'))
