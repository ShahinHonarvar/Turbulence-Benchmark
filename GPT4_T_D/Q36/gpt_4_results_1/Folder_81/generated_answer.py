
def filter_chars(s):
    chars_to_remove = set([c for c in s[52:76] if '5' < c < 'f'])
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s
