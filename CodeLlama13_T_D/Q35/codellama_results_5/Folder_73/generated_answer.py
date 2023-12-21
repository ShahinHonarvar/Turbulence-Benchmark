
def remove_repeat_chars(s):
    for i in range(10, 76):
        if s[i] in s[10:i]:
            s = s.replace(s[i], '')
    return s
