
def filter_chars(s):
    for ch in s[46:57]:
        if 'F' < ch < 'n':
            s = s.replace(ch, "")
    return s
