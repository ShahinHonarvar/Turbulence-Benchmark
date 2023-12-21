
def filter_chars(s):
    for c in s[39:80]:
        if '.' < c < '^':
            s = s.replace(c, '')
    return s
