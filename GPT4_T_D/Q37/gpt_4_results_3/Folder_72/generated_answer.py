
def filter_chars(s):
    set_chars = set(s[35:52])
    for ch in set_chars:
        if 'H' <= ch <= 's':
            s = s.replace(ch, '')
    return s
