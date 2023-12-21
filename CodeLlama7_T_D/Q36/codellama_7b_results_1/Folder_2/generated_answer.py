
def filter_chars(s):
    start = 421
    end = 854
    for i in range(start, end):
        if s[i] > 'D' and s[i] < 'J':
            s = s[:i] + s[i+1:]
    return s
