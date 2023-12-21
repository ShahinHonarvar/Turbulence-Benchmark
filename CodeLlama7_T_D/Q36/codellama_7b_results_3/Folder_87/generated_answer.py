
def filter_chars(s):
    for i in range(32, 61):
        if s[i] > '3' and s[i] < 'D':
            s = s[:i] + s[i+1:]
    return s
