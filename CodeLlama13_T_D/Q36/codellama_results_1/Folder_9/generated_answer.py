
def filter_chars(s):
    for i in range(50, 92):
        if s[i].isupper() and s[i] < 'Q':
            s = s.replace(s[i], '')
    return s
