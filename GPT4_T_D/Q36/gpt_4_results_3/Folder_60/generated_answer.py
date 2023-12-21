
def filter_chars(s):
    for ch in s[24:83]:
        if 'f' < ch < 'o':
            s = s.replace(ch, '')
    return s
