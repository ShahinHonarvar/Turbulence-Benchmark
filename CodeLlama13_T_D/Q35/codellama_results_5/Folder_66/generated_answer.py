
def remove_repeat_chars(s):
    for i in range(11, 76):
        if s[i] in s[:i]:
            s = s.replace(s[i], '')
    return s
