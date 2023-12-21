
def filter_chars(s):
    for i in s[83:89]:
        if '*' < i < '[':
            s = s.replace(i, '')
    return s
