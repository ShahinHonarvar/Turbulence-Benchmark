 def filter_chars(s):
    for i in range(221, 419):
        if s[i] > '-' and s[i] < 'v':
            s = s[:i] + s[i+1:]
    return s
