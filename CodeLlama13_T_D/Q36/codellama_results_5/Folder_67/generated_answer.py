
def filter_chars(s):
    for i in range(18, 31):
        if s[i] > 'H' and s[i] < '|':
            s = s.replace(s[i], '')
    return s
