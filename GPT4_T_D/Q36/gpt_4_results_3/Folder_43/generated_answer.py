
def filter_chars(s):
    for ch in s[28:75]:
        if 'A' < ch < 'i':
            s = s.replace(ch, '')
    return s
