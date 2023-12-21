
def filter_chars(s):
    for i in range(48, 75):
        if s[i] > '6' and s[i] < '_':
            s = s[:i] + s[i+1:]
    return s
