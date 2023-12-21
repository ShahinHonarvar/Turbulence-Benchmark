def remove_repeat_chars(s):
    for i in range(51, 76):
        s = s.replace(s[i], "")
    return s
