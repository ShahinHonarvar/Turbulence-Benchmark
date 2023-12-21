
def filter_chars(s):
    for ch in s[2:7]:
        if '3' < ch < '^':
            s = s.replace(ch, '')
    return s
