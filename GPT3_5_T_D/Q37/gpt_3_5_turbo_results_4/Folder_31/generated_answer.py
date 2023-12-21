
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 57 or i > 96 or c < '<' or c > 'w')
