
def filter_chars(s):
    for ch in s[83:89]:
        if '*' < ch < '[':
            s = s.replace(ch, '')
    return s
