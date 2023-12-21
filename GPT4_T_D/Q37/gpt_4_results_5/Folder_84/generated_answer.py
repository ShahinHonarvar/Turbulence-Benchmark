
def filter_chars(s):
    string_range = s[138:921]
    chars_to_remove = {c for c in string_range if '6' <= c <= 'A'}
    return ''.join(c for c in s if c not in chars_to_remove)
