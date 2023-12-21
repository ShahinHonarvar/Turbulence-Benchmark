
def remove_repeat_chars(s):
    for i in range(29, 53):
        if s[i].count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s
