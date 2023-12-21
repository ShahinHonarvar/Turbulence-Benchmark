
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if (i < 12 or i > 77) or (c < ':' or c > 'L')])
