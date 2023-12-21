
def filter_chars(s):
    for i in range(669, 888):
        if s[i].isalpha() and s[i] > 'B' and s[i] < 'Y':
            s = s.replace(s[i], '')
    return s
