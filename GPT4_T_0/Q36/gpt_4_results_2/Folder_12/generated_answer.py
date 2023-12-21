
def filter_chars(s):
    for i in range(33, 84):
        if 'm' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s
