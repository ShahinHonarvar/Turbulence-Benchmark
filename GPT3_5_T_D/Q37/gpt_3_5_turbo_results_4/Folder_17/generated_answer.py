
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 27 or i > 29 or c < ';' or c > 'b')
