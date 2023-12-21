
def filter_chars(string):
    removal_chars = set([c for i, c in enumerate(string) if 72 <= i <= 94 and '.' <= c <= 'b'])
    return ''.join([c for c in string if c not in removal_chars])
