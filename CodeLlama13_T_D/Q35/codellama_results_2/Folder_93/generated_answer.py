
def remove_repeat_chars(s):
    for i in range(57, 85):
        c = s[i]
        if s[i:].count(c) > 1:
            s = s.replace(c, "")
    return s
