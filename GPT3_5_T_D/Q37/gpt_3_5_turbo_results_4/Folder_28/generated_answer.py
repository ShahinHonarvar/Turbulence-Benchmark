
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if (20 <= i <= 79) and ('!' <= c <= 'T')])
