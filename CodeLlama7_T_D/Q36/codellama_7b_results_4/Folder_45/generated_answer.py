 def filter_chars(s):
    for i in range(81, 86):
        if s[i] > '!' and s[i] < 's':
            s = s[:i] + s[i+1:]
    return s
