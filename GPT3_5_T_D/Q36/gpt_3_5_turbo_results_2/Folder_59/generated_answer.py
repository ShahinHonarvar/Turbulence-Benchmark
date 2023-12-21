
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 3 or i >= 8 or c <= '?' or c >= 'k'])
