
def filter_chars(s):
    chars_to_remove = [c for c in s[3:7] if 'h' < c < 'k']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
