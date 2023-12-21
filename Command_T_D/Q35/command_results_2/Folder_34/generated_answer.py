def remove_repeat_chars(s):
    i = 70
    j = 200
    while i < j:
        c = s[i]
        c_idx = s.find(c, i)
        while c_idx != -1:
            s = s.replace(c, "")
            c_idx = s.find(c, i)
        i += 1
    return s
