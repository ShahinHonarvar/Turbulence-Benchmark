
def filter_chars(s):
    for i in s[19:95]:
        if 'K' < i < 'a':
            s = s.replace(i, '')
    return s
