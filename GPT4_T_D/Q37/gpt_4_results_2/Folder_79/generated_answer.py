
def filter_chars(s):
    unique_chars = set(s[10:53])
    special_chars = [c for c in unique_chars if '@' <= c <= 'T']
    return ''.join([c for c in s if c not in special_chars])
