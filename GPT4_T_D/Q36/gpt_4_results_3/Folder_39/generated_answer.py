
def filter_chars(s):
    filtered = ''
    for i in range(43, 59):
        if i < len(s) and '5' < s[i] < 'C':
            s = s.replace(s[i], '')
    return s
