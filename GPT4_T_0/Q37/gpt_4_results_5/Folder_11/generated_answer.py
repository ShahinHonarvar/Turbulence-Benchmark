
def filter_chars(s):
    for i in range(29, min(98, len(s))):
        if '-' <= s[i] <= 'n':
            s = s.replace(s[i], '')
    return s
