
def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[10:53]) if '@' <= c <= 'T']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
