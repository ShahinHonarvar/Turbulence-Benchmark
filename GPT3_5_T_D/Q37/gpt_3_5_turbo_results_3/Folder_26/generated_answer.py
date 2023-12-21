
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if i < 20 or i > 62 or c < 'i' or c > 'k')
