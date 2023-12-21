
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if (i < 42 or i > 97) or (c < '*' or c > 'b'))
