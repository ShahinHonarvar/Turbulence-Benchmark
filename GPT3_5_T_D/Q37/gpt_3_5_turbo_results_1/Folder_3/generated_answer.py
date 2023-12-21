
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 37 or i > 56 or c < '6' or c > '_'])
