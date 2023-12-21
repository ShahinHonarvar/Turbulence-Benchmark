
def remove_repeat_chars(s):
    s = list(s)
    for i in range(6):
        c = s[i]
        if s.count(c) > 1:
            s.remove(c)
    return "".join(s)
