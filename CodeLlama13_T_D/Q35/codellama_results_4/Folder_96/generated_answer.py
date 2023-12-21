
def remove_repeat_chars(s):
    for i in range(60, 200):
        if s[i] in s[60:i]:
            s = s.replace(s[i], "")
    return s
