
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if i < 331 or i >= 713 or c <= 'M' or c >= '_')
