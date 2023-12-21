
def filter_chars(s):
    chars_to_remove = {c for c in s[39:81] if '.' < c < '^'}
    return ''.join(c for c in s if c not in chars_to_remove)
