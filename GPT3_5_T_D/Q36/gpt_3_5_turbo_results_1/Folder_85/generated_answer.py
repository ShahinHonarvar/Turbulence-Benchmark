
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (55 <= i < 80 and 'S' < c < 's')])
