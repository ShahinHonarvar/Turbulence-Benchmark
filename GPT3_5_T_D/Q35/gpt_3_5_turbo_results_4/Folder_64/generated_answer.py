
def remove_repeat_chars(s):
    for i in range(1, 5):
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s
