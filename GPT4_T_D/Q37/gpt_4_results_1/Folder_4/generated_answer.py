
def filter_chars(s):
    constrained_chars = [c for c in s[19:34] if 'S' <= c <= '{']
    return ''.join([c for c in s if c not in constrained_chars])
