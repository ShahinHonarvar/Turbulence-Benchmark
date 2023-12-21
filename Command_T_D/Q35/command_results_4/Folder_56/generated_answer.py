def remove_repeat_chars(s):
    i = 7
    j = 9
    while i < j:
        c = s[i]
        if s.count(c) > 2:
            s = s.replace(c, "")
            i += 1
        else:
            i += 1
    return s
