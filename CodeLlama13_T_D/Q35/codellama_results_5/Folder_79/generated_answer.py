
def remove_repeat_chars(s):
    for i in range(1, 7):
        if s[i-1] != s[i] and s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s
