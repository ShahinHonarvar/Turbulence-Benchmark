def filter_chars(s):
    for i in range(421, 854):
        if s[i] > 'D' and s[i] < 'J':
            s = s.replace(chr(i), '')
    return s
