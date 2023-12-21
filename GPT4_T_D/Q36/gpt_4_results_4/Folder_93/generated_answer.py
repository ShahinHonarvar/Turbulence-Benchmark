
def filter_chars(s):
    for ch in s[53:88]:
        if '&' < ch < 'c':
            s = s.replace(ch, '')
    return s
