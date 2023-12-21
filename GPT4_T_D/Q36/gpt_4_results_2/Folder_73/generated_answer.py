
def filter_chars(s):
    filtered_chars = {c for i, c in enumerate(s) if 66 < i < 90 and '#' < c < 'T'}
    return ''.join(c for c in s if c not in filtered_chars)
