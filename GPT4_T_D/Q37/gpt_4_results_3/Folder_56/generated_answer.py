
def filter_chars(s):
    to_remove = set([c for i, c in enumerate(s) if 71 <= i <= 94 and 'K' <= c <= 'a'])
    
    return ''.join([c for c in s if c not in to_remove])
