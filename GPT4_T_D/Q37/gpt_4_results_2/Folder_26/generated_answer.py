
def filter_chars(s):
    chars_to_remove = set(c for c in s[20:63] if 'i' <= c <= 'k')
    return ''.join(c for c in s if c not in chars_to_remove)
