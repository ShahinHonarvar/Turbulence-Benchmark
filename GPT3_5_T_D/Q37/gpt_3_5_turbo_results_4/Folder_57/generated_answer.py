
def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 27 or i > 85 or c < '!' or c > 'B'])
