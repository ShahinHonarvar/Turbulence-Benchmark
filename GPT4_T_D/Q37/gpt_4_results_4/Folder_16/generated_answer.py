
def filter_chars(s):
    selected_chars = set([c for c in s[225:382] if 'D' <= c <= 'Y'])
    return ''.join([c for c in s if c not in selected_chars])
