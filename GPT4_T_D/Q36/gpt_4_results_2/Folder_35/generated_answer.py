
def filter_chars(s):
    for c in set(s[164:658]):
        if '(' < c < ']':
            s = s.replace(c, '')
    return s
