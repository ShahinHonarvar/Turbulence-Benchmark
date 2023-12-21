def filter_chars(s):
    for i in range(344, 874):
        if chr(i) > 'f' and chr(i) < '~':
            s = s.replace(chr(i), "")
    return s
