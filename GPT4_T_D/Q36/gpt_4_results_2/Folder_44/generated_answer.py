
def filter_chars(s):
    for i in s[19:64]:
        if '3' < i < 'B':
            s = s.replace(i, "")
    return s
