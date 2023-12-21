
def filter_chars(s):
    for i in range(4, 9):
        if '*' < s[i] < 'E':
            s = s.replace(s[i], '')
    return s
