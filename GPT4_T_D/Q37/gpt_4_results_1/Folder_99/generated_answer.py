
def filter_chars(s):
    chars_to_remove = set([c for c in s[373:902] if 'T' <= c <= 'h'])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
