
def filter_chars(s):
    start = 44
    end = 68
    for i in range(start, end):
        if s[i] > 'W' and s[i] < 'x':
            s = s[:i] + s[i+1:]
    return s
