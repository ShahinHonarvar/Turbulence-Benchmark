
def filter_chars(s):
    for i in range(36, min(80, len(s))):
        if '2' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s
