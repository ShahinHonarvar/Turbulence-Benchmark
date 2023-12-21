
def filter_chars(s):
    for i in range(4):
        if s[i] > '$' and s[i] < '?':
            s = s.replace(s[i], '')
    return s
