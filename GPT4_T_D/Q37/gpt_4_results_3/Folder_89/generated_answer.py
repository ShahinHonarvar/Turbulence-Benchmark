
def filter_chars(s):
    removed_chars = {c for i, c in enumerate(s) if 11 <= i <= 32 and '!' <= c <= '@'}
    return ''.join(c for c in s if c not in removed_chars)
