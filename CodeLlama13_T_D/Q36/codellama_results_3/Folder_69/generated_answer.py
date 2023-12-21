
def filter_chars(s):
    for i in range(343, 665):
        if s[i] > '%' and s[i] < 'U':
            s = s.replace(s[i], '')
    return s
