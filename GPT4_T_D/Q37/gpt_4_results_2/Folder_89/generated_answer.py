
def filter_chars(s):
    for i in range(11, min(len(s), 33)):
        if '!' <= s[i] <= '@':
            s = s.replace(s[i], '')
    return s
