
def filter_chars(s):
    chars_to_remove = [c for c in s[27:30] if ';' <= c <= 'b']
    return ''.join(c for c in s if c not in chars_to_remove)
