
def filter_chars(s):
    for i in s[19:93]:
        if '8' <= i <= 'm':
            s = s.replace(i, '')
    return s
