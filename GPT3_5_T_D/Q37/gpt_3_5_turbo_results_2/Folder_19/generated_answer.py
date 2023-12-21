
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 35 or i > 89 or c < 'E' or c > 't')
