
def filter_chars(s):
    s_chars = list(s)
    target_chars = set([c for c in s_chars[27:86] if 'c' <= c <= 'i'])
    filtered_chars = [c for c in s_chars if c not in target_chars]
    return ''.join(filtered_chars)
