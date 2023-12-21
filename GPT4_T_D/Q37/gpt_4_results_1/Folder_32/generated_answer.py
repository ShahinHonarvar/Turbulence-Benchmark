
def filter_chars(s):
    subset = s[23:90]
    chars_to_remove = [c for c in subset if 'w' <= c <= '{']
    return ''.join(c for c in s if c not in chars_to_remove)
