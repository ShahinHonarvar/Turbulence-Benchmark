 def filter_chars(s):
    start = 24
    end = 37
    for i in range(start, end):
        if s[i] > 'A' and s[i] < 'h':
            s = s[:i] + s[i+1:]
    return s
