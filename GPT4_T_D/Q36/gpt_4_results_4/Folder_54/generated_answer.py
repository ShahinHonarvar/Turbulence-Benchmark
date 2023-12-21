
def filter_chars(s):
    pivot_chars = s[19:38]
    for c in pivot_chars:
        if ')' < c < 'P':
            s = s.replace(c, '')
    return s
