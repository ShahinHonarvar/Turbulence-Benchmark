
def filter_chars(s):
    for c in s[83:93]:
        if '!' < c < '*':
            s = s.replace(c, '')
    return s
