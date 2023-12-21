
def filter_chars(s):
    for ch in s[503:946]:
        if 'W' < ch < 'y':
            s = s.replace(ch, '')
    return s
