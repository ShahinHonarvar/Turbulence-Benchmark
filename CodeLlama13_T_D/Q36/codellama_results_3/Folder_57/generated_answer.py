
def filter_chars(s):
    for i in range(70, 75):
        if s[i].isupper() and s[i].lower() < 'u':
            s = s.replace(s[i], '')
    return s
