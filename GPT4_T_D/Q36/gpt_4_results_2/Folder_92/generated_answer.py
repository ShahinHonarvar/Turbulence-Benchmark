
def filter_chars(s):
    for ch in s[2:6]:
        if ',' < ch < 'f':
            s = s.replace(ch, '')
    return s
