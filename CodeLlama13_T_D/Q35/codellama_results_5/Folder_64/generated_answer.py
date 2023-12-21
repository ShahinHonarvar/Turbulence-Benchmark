
def remove_repeat_chars(s):
    for i in range(6):
        c = s[i]
        if s.count(c) > 1 and i < 5:
            s = s.replace(c, "")
    return s
