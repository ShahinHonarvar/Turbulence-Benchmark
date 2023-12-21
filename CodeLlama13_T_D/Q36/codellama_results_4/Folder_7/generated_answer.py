
def filter_chars(s):
    for i in range(502, 946):
        if s[i].isalpha() and s[i] > 'W' and s[i] < 'y':
            s = s.replace(s[i], '')
    return s
