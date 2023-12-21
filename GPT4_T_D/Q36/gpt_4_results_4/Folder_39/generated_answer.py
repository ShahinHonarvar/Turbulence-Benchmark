
def filter_chars(s):
    for i in range(44, 59):
        if '5' < s[i] < 'C':
            s = s.replace(s[i], '')
    return s
