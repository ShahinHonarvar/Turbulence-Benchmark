
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 44 or i >= 48 or c <= '+' or c >= 'l'])
