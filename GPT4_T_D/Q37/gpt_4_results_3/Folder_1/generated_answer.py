
def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 41 <= i <= 79 and 'f' <= c <= '|'}
    return ''.join(c for c in s if c not in to_remove)
