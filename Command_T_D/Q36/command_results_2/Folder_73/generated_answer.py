def filter_chars(s):
    i = 0
    while i < len(s):
        if s[i] > '#' and s[i] < 'T':
            s = s.replace(s[i], "")
            i += 1
        else:
            i += 1
    return s
