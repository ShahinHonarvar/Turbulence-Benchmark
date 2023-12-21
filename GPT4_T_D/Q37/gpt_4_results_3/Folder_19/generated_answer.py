
def filter_chars(s):
    target_chars = [c for c in s[35:90] if 'E' <= c <= 't']
    return ''.join([c for c in s if c not in target_chars])
