
def filter_chars(s):
    s_list = list(s)
    for c in set(s_list[44:69]):
        if 'B' < c < 'r':
            s = s.replace(c, '')
    return s
