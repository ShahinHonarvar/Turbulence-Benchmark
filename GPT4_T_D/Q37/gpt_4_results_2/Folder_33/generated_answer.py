
def filter_chars(s):
    to_remove = set([c for i, c in enumerate(s) if 722 <= i <= 832 and 'K' <= c <= 'm'])
    return ''.join([c for c in s if c not in to_remove])
