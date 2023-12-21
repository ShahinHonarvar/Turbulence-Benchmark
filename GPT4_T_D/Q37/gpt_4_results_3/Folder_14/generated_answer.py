
def filter_chars(string):
    to_remove = set([c for i, c in enumerate(string) if 35 <= i <= 98 and 'A' <= c <= 'b'])
    return ''.join([c for c in string if c not in to_remove])
