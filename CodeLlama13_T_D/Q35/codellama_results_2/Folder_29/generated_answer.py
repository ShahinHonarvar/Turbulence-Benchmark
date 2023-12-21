
def remove_repeat_chars(s):
    for i in range(70, 98):
        c = s[i]
        if s.count(c) > 1:
            s = s.replace(c, '')
    return s
