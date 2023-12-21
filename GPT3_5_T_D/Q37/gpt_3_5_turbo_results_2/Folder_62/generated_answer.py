
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 10 or i > 69 or c < 'I' or c > 'K'])
