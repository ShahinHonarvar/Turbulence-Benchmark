
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 23 or i > 89 or not ('w' <= c <= '{')])
