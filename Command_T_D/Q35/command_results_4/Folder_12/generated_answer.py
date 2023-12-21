def remove_repeat_chars(s):
    new = ""
    for i in range(16, 87):
        c = s[i]
        if c in s[16:]:
            s = s.replace(c, "")
        else:
            new += c
    return s + new
