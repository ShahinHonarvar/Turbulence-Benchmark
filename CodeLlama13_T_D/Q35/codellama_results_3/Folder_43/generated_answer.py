
def remove_repeat_chars(s):
    for i in range(10, 28):
        if s[i] in s[10:28]:
            s = s.replace(s[i], '')
    return s
