
def filter_chars(s):
    for i in range(42, 68):
        if s[i] > 't' and s[i] < 'x':
            s = s[:i] + s[i+1:]
    return s
