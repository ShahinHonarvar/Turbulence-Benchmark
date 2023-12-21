
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 57 or i >= 69 or not '(' < c < 'W'])
