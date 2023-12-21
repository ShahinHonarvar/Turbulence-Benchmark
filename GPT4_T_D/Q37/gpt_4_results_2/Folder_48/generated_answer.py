
def filter_chars(s):
    for i in range(513, 878):
        if '?' <= s[i] <= 'n':
            s = s.replace(s[i], '')
    return s
