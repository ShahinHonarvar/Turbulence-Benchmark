
def filter_chars(s):
    to_remove = set(x for x in s[72:95] if '.' <= x <= 'b')
    return ''.join(ch for ch in s if ch not in to_remove)
