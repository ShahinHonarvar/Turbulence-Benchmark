def filter_chars(s):
    for i in range(26, 81):
        if s[i] > '<' and s[i] < '>':
            s = s.replace(chr(i), '')
    return s
