
def filter_chars(s):
    for i in range(171, 195):
        if '!' < s[i] < '}':
            s = s.replace(s[i], '')
    return s
