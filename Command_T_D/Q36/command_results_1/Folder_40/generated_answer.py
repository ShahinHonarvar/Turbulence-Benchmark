def filter_chars(s):
    i = 0
    while i < len(s) - 7:
        if s[i] in '-L':
            s = s.replace(s[i], "")
            i += 1
    return s
