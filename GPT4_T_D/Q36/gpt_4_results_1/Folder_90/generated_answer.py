
def filter_chars(s):
    chars_to_remove  = [c for c in s[345:874] if 'f' < c < '~']
    for ch in set(chars_to_remove):
        s = s.replace(ch, '')
    return s
