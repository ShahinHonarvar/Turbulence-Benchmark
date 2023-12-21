
def filter_chars(s):
    substr = s[18:82]
    chars_to_remove = [c for c in substr if 'W' <= c <= '[']
    return ''.join(c for c in s if c not in chars_to_remove)
