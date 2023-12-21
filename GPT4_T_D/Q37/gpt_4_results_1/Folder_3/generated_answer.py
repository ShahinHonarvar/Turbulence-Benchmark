
def filter_chars(s):
    target_chars = set(ch for ch in s[37:57] if '6' <= ch <= '_')
    return ''.join(ch for ch in s if ch not in target_chars)
