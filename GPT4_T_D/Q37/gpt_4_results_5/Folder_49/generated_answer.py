
def filter_chars(s):
    remove_chars = {c for i, c in enumerate(s) if 42 <= i <= 97 and '*' <= c <= 'b'}
    return ''.join(c for c in s if c not in remove_chars)
