 def filter_chars(s):
    for i in range(309, 591):
        if s[i] > 'S' and s[i] < 'm':
            s = s[:i] + s[i+1:]
    return s
