
def filter_chars(s):
    for i in range(10, 15):
        if s[i].lower() > 't' and s[i].lower() < 'v':
            s = s.replace(s[i], '')
    return s
