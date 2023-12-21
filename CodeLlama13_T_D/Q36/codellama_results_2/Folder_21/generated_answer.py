
def filter_chars(s):
    for i in range(219, 403):
        if s[i] > '*' and s[i] < '7':
            s = s.replace(s[i], '')
    return s
