
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if (i < 373 or i > 901 or c < 'T' or c > 'h')])
