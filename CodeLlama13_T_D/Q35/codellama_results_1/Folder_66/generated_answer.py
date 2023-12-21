
def remove_repeat_chars(s):
    for i in range(11, 76):
        c = s[i]
        if s.count(c) > 1:
            s = s.replace(c, "")
    return s
