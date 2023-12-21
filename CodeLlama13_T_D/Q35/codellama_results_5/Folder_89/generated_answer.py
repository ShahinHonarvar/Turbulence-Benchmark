
def remove_repeat_chars(s):
    for i in range(55, 84):
        c = s[i]
        if s.count(c) > 1:
            s = s.replace(c, "")
    return s
