
def filter_chars(s):
    for ch in s[15:75]:
        if '9' < ch < 'K':
            s = s.replace(ch, "")
    return s
