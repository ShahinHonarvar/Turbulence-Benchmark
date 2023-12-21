
def filter_chars(s):
    for i in range(59, 81):
        if s[i] > '5' and s[i] < '>':
            s = s.replace(s[i], '')
    return s
