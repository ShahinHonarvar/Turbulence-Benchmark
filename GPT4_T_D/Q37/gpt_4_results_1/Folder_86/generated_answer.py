
def filter_chars(str):
    to_remove = set([c for i, c in enumerate(str) if (164 <= i <= 706) and 'O' <= c <= '}'])
    return ''.join([c for c in str if c not in to_remove])
