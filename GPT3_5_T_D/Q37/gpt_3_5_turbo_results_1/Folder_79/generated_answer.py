
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 10 or i > 52 or c < "@" or c > "T")
