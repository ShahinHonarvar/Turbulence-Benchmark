 def filter_chars(s):
    for i in range(38, 81):
        if s[i] > '.' and s[i] < '^':
            s = s[:i] + s[i+1:]
    return s
