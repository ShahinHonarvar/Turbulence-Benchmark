
def filter_chars(s):
    for i in range(19, min(91, len(s))):
        if 'F' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s
