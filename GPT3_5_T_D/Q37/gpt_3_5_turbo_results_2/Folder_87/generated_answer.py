
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 18 or i > 81 or c < 'W' or c > '['])
