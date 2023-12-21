 def filter_chars(s):
    for i in range(31, 73):
        if s[i] > 'M' and s[i] < 'j':
            s = s[:i] + s[i+1:]
    return s
