
def filter_chars(str):
    removal_chars = set(c for i, c in enumerate(str) if 41 <= i <= 64 and 'K' <= c <= ']')
    return ''.join(c for c in str if c not in removal_chars)
