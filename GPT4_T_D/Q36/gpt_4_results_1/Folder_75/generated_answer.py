
def filter_chars(s):
    for ch in s[47:74]:
        if '&' < ch < 'M':
            s = s.replace(ch, '')
    return s
