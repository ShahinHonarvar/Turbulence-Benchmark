
def filter_chars(s):
    for c in s[59:81]:
        if '5' < c < '>':
            s = s.replace(c, '')
    return s
