
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 31 or i > 38 or c < ';' or c > 'g')
