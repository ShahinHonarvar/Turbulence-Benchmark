
def filter_chars(s):
    for i in range(73, 93):
        if s[i] > '<' and s[i] < 'J':
            s = s.replace(s[i], '')
    return s
