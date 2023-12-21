
def filter_chars(s):
    s_list = list(s)
    for c in s_list[319:337]:
        if 'B' < c < 'z':
            s = s.replace(c, '')
    return s
