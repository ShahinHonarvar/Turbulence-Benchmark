
def filter_chars(s):
    chars = []
    for i in range(32, 61):
        if s[i] > '3' and s[i] < 'D':
            while s[i] in s:
                s = s.replace(s[i], '')
    return s
