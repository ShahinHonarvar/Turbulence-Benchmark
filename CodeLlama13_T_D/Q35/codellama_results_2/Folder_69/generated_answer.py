
def remove_repeat_chars(s):
    for i in range(39, 43):
        if s[i].count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s
