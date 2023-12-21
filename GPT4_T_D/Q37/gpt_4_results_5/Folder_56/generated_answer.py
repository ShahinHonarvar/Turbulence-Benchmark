
def filter_chars(s):
    for i in range(71, 95):
        if i < len(s) and 'K' <= s[i] <= 'a':
            s = s.replace(s[i], '')
    return s
