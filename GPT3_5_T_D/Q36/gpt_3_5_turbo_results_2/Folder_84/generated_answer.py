
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 171 or i >= 636 or c <= 'c' or c >= 's')
