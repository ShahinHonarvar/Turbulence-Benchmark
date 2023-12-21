
def filter_chars(s):
    for ch in s[29:80]:
        if 'K' <= ch <= 'z':
            s = s.replace(ch, "")
    return s
