
def filter_chars(s):
    for i in range(225, 381):
        if s[i].lower() >= 'd' and s[i].lower() <= 'y':
            s = s.replace(s[i], '')
    return s
