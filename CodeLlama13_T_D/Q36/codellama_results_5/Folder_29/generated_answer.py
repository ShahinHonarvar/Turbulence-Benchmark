
def filter_chars(s):
    for i in range(46, 68):
        if s[i].isalpha() and s[i] > 'H' and s[i] < 's':
            s = s.replace(s[i], '')
    return s
