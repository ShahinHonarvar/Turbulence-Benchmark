
def filter_chars(s):
    for i in range(12, min(89, len(s))):
        if '&' <= s[i] <= 'v':
            s = s.replace(s[i], '')
    return s
