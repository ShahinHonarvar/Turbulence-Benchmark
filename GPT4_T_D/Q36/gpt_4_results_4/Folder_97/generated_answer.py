
def filter_chars(s):
    for ch in s[310:591]:
        if 'S' < ch < 'm':
            s = s.replace(ch, "")
    return s
