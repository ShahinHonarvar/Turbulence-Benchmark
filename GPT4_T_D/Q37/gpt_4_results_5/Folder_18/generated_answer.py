
def filter_chars(string):
    target_chars = set(x for x in string[770:971] if '-' <= x <= 'D')
    return ''.join([c for c in string if c not in target_chars])
