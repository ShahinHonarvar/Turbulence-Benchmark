
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 19 or i > 33 or c < 'S' or c > '{')
