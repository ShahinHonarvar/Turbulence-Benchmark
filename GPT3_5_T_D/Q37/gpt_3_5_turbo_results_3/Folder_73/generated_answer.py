
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 22 or i > 85 or c < '7' or c > 'e')
