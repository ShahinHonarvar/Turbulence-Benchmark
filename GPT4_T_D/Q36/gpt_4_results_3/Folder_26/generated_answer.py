
def filter_chars(s):
    for i in s[44:83]:
        if ':' < i < 'Q':
            s = s.replace(i, '')
    return s
