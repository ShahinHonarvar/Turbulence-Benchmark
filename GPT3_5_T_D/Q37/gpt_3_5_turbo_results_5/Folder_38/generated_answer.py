
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 24 or i > 79 or c < 'a' or c > 'f')
