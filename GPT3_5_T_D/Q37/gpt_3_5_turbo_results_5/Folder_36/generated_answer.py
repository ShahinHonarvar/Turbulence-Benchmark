
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 259 or i > 502 or c < ',' or c > '3')
