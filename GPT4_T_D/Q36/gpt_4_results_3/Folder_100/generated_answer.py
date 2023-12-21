
def filter_chars(s):
    for ch in s[44:69]:
        if 'B' < ch < 'r':
            s = s.replace(ch, '')
    return s
