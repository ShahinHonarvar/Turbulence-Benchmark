def remove_repeat_chars(s):
    c = s[44:67]
    i = s.index(c)
    j = s.rfind(c, i, i+len(c))
    while i < j:
        s = s.replace(c, '', 1)
        i = s.index(c)
        j = s.rfind(c, i, i+len(c))
    return s
