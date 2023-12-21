
def filter_chars(s):
    for i in s[220:403]:
        if '*' < i < '7':
            s = s.replace(i, '')
    return s
