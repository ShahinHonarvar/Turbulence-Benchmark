
def filter_chars(s):
    remove_chars = set(ch for ch in s[72:95] if '.' <= ch <= 'b')
    return ''.join(ch for ch in s if ch not in remove_chars)
