def remove_repeat_chars(s):
    i = 20
    j = 43
    while i < j:
        c = s[i]
        if s.count(c) > 1:
            s = s.replace(c, "")
        i += 1
    return s
